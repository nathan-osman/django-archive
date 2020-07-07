from datetime import datetime
from io import BytesIO
from json import dump
from os import path

from django.apps.registry import apps
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import models

from ... import __version__
from ...archivers import get_archiver, TARBALL_BZ2


class Command(BaseCommand):
    """
    Create a compressed archive of database tables and uploaded media.
    """

    help = "Create a compressed archive of database tables and uploaded media."

    @staticmethod
    def _get_base_filename(archiver, fmt):
        """
        Derive the base filename for the archive
        """
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
                archiver.get_extension(fmt),
            ),
        )

    @staticmethod
    def _add_to_archive(archive, filename, fileobj):
        """
        Add the filename / fileobj to the archive
        """
        size = fileobj.tell()
        fileobj.seek(0)
        archive.add(filename, size, fileobj)

    @staticmethod
    def _dump_db(archive):
        """
        Write database data to the archive
        """

        # Determine the list of models to exclude
        exclude = getattr(settings, 'ARCHIVE_EXCLUDE', (
            'auth.Permission',
            'contenttypes.ContentType',
            'sessions.Session',
        ))

        # TODO: use a temp file to avoid excess memory usage

        # Dump the tables
        data = BytesIO()
        call_command(
            'dumpdata',
            all=True,
            format='json',
            exclude=exclude,
            stdout=data,
        )

        # Write the data to the archive
        Command._add_to_archive(archive, 'data.json', data)

    @staticmethod
    def _dump_files(archive):
        """
        Dump all uploaded media to the archive
        """

        # Loop through all models and find FileFields
        for model in apps.get_models():

            # Find all FileFields in the model
            field_names = []
            for field in model._meta.fields:
                if isinstance(field, models.FileField):
                    field_names.append(field.name)

            # If there aren't any FileFields, quit
            if not field_names:
                return

            # Loop through each row, saving the files
            for row in model.objects.all():
                for field_name in field_names:
                    field = getattr(row, field_name)
                    if field:
                        with field as field:
                            archive.addfile(field.name, field.size, field)

    @staticmethod
    def _dump_meta(archive):
        """
        Dump metadata to the archive
        """
        data = BytesIO()
        dump({'version': __version__}, data)
        Command._add_to_archive(archive, 'meta.json', data)

    # pylint: disable=unused-argument
    def handle(self, *args, **kwargs):
        """
        Process the command
        """
        fmt = getattr(settings, 'ARCHIVE_FORMAT', TARBALL_BZ2)
        archiver = get_archiver(fmt)
        filename = Command._get_base_filename(archiver, fmt)
        with open(filename, 'w') as fileobj:
            with archiver(fileobj, fmt) as archive:
                Command._dump_db(archive)
                Command._dump_files(archive)
                Command._dump_meta(archive)
        self.stdout.write(
            self.style.SUCCESS(
                "Successfully wrote {}".format(archive.get_filename),
            ),
        )
