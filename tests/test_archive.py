from django.core.management import call_command
from django.test import TestCase

from django_archive import archivers

from .sample.models import Sample


class ArchiveTestCase(TestCase):
    """
    Test that the archive command executes correctly
    """

    def setUp(self):
        """
        Create an empty model instance
        """
        Sample().save()

    def test_archive_tar(self):
        """
        Test that an uncompressed tarball is created
        """
        with self.settings(ARCHIVE_FORMAT=archivers.TARBALL):
            call_command('archive')

    def test_archive_zip(self):
        """
        Test that a ZIP file is created
        """
        with self.settings(ARCHIVE_FORMAT=archivers.ZIP):
            call_command('archive')
