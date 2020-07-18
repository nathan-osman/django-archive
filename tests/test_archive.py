from json import load

from django_archive import __version__

from .base import BaseArchiveTestCase
from .sample.models import Sample


class ArchiveTestCase(BaseArchiveTestCase):
    """
    Test that the archive command includes correct data in the archive
    """

    def setUp(self):
        Sample().save()
        super().setUp()

    def test_data(self):
        """
        Confirm that the model was archived
        """
        with self.tarfile.extractfile('data.json') as fileobj:
            data = load(fileobj)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['model'], 'sample.sample')

    def test_meta(self):
        """
        Confirm that meta information is present
        """
        with self.tarfile.extractfile('meta.json') as fileobj:
            data = load(fileobj)
            self.assertEqual(data['version'], __version__)
