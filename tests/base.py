from contextlib import ExitStack
from tempfile import TemporaryDirectory

from django.test import TestCase


class BaseTestCase(TestCase):
    """
    Base class for tests
    """

    def setUp(self):
        """
        Initialize the test by setting up a temporary directory
        """
        with ExitStack() as stack:
            self.directory = stack.enter_context(TemporaryDirectory())
            stack.enter_context(
                self.settings(ARCHIVE_DIRECTORY=self.directory),
            )
            self.addCleanup(stack.pop_all().close)
