from contextlib import ExitStack
from os import path
from tarfile import TarFile
from tempfile import TemporaryDirectory

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
                self.settings(
                    ARCHIVE_DIRECTORY=self.directory,
                    MEDIA_ROOT=self.directory,
                ),
            )
            self.addCleanup(stack.pop_all().close)


class BaseArchiveTestCase(BaseTestCase):
    """
    Base class for tests that require the creation of a single archive
    """

    _FILENAME = 'test'
    _FORMAT_ID = archivers.TARBALL
    _FORMAT = archivers.registry.get(_FORMAT_ID)

    def setUp(self):
        """
        Initialize the test by initializing settings for creating an archive
        """
        super().setUp()
        stack = ExitStack()
        stack.enter_context(
            self.settings(
                ARCHIVE_FILENAME=self._FILENAME,
                ARCHIVE_FORMAT=self._FORMAT_ID,
            ),
        )
        self.addCleanup(stack.close)

    def open_archive(self):
        """
        The archive is available for reading in self.tarfile. To populate the
        database, override this method and call super().setUp() after.
        """
        stack = ExitStack()
        # pylint: disable=attribute-defined-outside-init
        self.tarfile = stack.enter_context(
            TarFile.open(
                path.join(
                    self.directory,
                    '{}.{}'.format(
                        self._FILENAME,
                        self._FORMAT.extensions[0],
                    ),
                ),
            ),
        )
        self.addCleanup(stack.close)
