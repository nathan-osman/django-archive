from contextlib import contextmanager
from tempfile import TemporaryDirectory

from django.core.management import call_command
from django.test import TestCase

from django_archive import archivers


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

    @contextmanager
    def _wrap_in_temp_dir(self):
        with TemporaryDirectory() as directory:
            yield self.settings(ARCHIVE_DIRECTORY=directory)

    def test_archive(self):
        """
        Test each format
        """
        for fmt in self._FORMATS:
            with self.subTest(fmt=fmt):
                with self._wrap_in_temp_dir():
                    with self.settings(ARCHIVE_FORMAT=fmt):
                        call_command('archive')
