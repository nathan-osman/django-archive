"""
Create an archive
"""

from contextlib import contextmanager
from datetime import datetime
from json import dump
from os import path

from django.apps import apps
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection, models
from django.db.migrations.recorder import MigrationRecorder

from ... import __version__
from ...archivers import registry, TARBALL_BZ2
from ...util.file import MixedModeTemporaryFile


class Command(BaseCommand):
    """
    Create a compressed archive of database tables and uploaded media.
    """

    help = "Create a compressed archive of database tables and uploaded media."

    _DEFAULT_ARCHIVE_EXCLUDE = (
        'auth.Permission',
        'contenttypes.ContentType',
        'sessions.Session',
    )

    @staticmethod
    def _get_filename(fmt):
        return path.join(
            getattr(settings, 'ARCHIVE_DIRECTORY', ''),
            "{}.{}".format(
                datetime.today().strftime(
                    getattr(
                        settings,
                        'ARCHIVE_FILENAME',
                        '%Y-%m-%d--%H-%M-%S',
                    ),
                ),
                fmt.extensions[0],
            ),
        )

    @staticmethod
    @contextmanager
    def _write_to_archive(archive, filename):
        with MixedModeTemporaryFile() as tempfile:
            with tempfile.open('w') as fileobj:
                yield fileobj
            tempfile.rewind()
            with tempfile.open('rb') as fileobj:
                archive.add(filename, tempfile.size(), fileobj)

    @staticmethod
    def _dump_meta(archive):
        with Command._write_to_archive(archive, 'meta.json') as fileobj:
            dump(
                {
                    'version': __version__,
                    'migrations': dict(
                        MigrationRecorder(connection)
                        .applied_migrations()
                        .keys()
                    ),
                },
                fileobj,
                indent=2,
            )

    @staticmethod
    def _dump_db(archive):
        with Command._write_to_archive(archive, 'data.json') as fileobj:
            call_command(
                'dumpdata',
                all=True,
                format='json',
                exclude=getattr(
                    settings,
                    'ARCHIVE_EXCLUDE',
                    Command._DEFAULT_ARCHIVE_EXCLUDE,
                ),
                stdout=fileobj,
            )

    @staticmethod
    def _dump_files(archive):
        for app_config in apps.get_app_configs():
            for model in app_config.get_models():
                field_names = []
                for field in model._meta.fields:
                    if isinstance(field, models.FileField):
                        field_names.append(field.name)
                if not field_names:
                    continue
                for row in model.objects.all():
                    for field_name in field_names:
                        field = getattr(row, field_name)
                        if field:
                            with field as field:
                                archive.add(field.name, field.size, field)

    # pylint: disable=unused-argument
    def handle(self, *args, **kwargs):
        """
        Process the command
        """
        fmt_id = getattr(settings, 'ARCHIVE_FORMAT', TARBALL_BZ2)
        fmt = registry.get(fmt_id)
        filename = Command._get_filename(fmt)
        with open(filename, 'wb') as fileobj:
            archive = fmt.archiver(fileobj, fmt_id)
            with archive:
                Command._dump_meta(archive)
                Command._dump_db(archive)
                Command._dump_files(archive)
        self.stdout.write(
            self.style.SUCCESS(
                "Successfully wrote {}".format(filename),
            ),
        )
