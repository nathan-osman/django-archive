from contextlib import ExitStack
from os import path
from tarfile import TarFile
from tempfile import TemporaryDirectory

from django.core.management import call_command
from django.test import TestCase
from django_archive import archivers


class BaseTestCase(TestCase):
    """
    Base class for tests
    """

    def setUp(self):
        """
        Initialize the test by setting up a temporary directory

        The directory is available in self.directory.
        """
        with ExitStack() as stack:
            self.directory = stack.enter_context(TemporaryDirectory())
            stack.enter_context(
                self.settings(ARCHIVE_DIRECTORY=self.directory),
            )
            self.addCleanup(stack.pop_all().close)


class BaseArchiveTestCase(BaseTestCase):
    """
    Base class for tests that require the creation of a single archive
    """

    _FILENAME = 'test'
    _FORMAT = archivers.TARBALL
    _ARCHIVER = archivers.get_archiver(_FORMAT)

    def setUp(self):
        """
        Initialize the test by creating an archive

        The archive is available for reading in self.tarfile. To populate the
        database, override this method and call super().setUp() after.
        """
        super().setUp()
        with ExitStack() as stack:
            stack.enter_context(
                self.settings(
                    ARCHIVE_FILENAME=self._FILENAME,
                    ARCHIVE_FORMAT=self._FORMAT,
                ),
            )
            call_command('archive')
            self.tarfile = stack.enter_context(
                TarFile.open(
                    path.join(
                        self.directory,
                        '{}.{}'.format(
                            self._FILENAME,
                            self._ARCHIVER.get_extension(self._FORMAT),
                        ),
                    ),
                ),
            )
            self.addCleanup(stack.pop_all().close)
