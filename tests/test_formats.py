from django.core.files.base import ContentFile
from django.core.management import call_command
from django.test import TestCase

from django_archive import archivers

from .sample.models import Sample


class FormatsTestCase(TestCase):
    """
    Test that the archive command works with all available formats
    """

    _FORMATS = (
        archivers.TARBALL,
        archivers.TARBALL_GZ,
        archivers.TARBALL_BZ2,
        archivers.TARBALL_XZ,
        archivers.ZIP,
    )

    def test_archive(self):
        """
        Test each format
        """
        for fmt in self._FORMATS:
            with self.subTest(fmt=fmt):
                with self.settings(ARCHIVE_FORMAT=fmt):
                    call_command('archive')
