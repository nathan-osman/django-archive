from django.core.management import call_command
from django.test import TestCase


class ArchiveTestCase(TestCase):
    """
    Test that the archive command executes correctly
    """

    def setUp(self):
        call_command(
            'archive',
        )

    def test_works(self):
        """
        Test that the command actually works
        """
