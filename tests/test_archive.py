from json import load

from django.core.files.base import ContentFile
from django_archive import __version__

from .base import BaseArchiveTestCase
from .sample.models import Sample


class ArchiveTestCase(BaseArchiveTestCase):
    """
    Test that the archive command includes correct data in the archive
    """

    _ATTACHMENT_FILENAME = 'sample.txt'
    _ATTACHMENT_CONTENT = b'sample'

    def setUp(self):
        sample = Sample()
        sample.attachment.save(
            self._ATTACHMENT_FILENAME,
            ContentFile(self._ATTACHMENT_CONTENT),
        )
        super().setUp()

    def test_data(self):
        """
        Confirm that the model and attached files were archived
        """
        with self.tarfile.extractfile('data.json') as fileobj:
            data = load(fileobj)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['model'], 'sample.sample')
        with self.tarfile.extractfile(data[0]['fields']['attachment']) as fileobj:
            content = fileobj.read()
        self.assertEqual(content, self._ATTACHMENT_CONTENT)

    def test_meta(self):
        """
        Confirm that meta information is present
        """
        with self.tarfile.extractfile('meta.json') as fileobj:
            data = load(fileobj)
            self.assertEqual(data['version'], __version__)
