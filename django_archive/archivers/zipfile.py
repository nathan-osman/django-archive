from zipfile import ZipFile


class ZipArchiver:
    """
    Archiver for creating ZIP files
    """

    # pylint: disable=unused-argument
    @staticmethod
    def get_extension(fmt):
        """
        Determine the correct file extension (always .zip)
        """
        return 'zip'

    # pylint: disable=unused-argument
    def __init__(self, fileobj, fmt):
        self._fileobj = fileobj

    def __enter__(self):
        # pylint: disable=attribute-defined-outside-init
        self._zipfile = ZipFile(
            file=self._fileobj,
            mode='w',
        )

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._zipfile.close()

    def add(self, filename, size, fileobj):
        """
        Add the provided file to the archive
        """
        # Loop through the contents of the fileobj,
        # writing them to the zipfile in chunks
        bytes_remaining = size
        with self._zipfile.open(filename, 'w') as cfile:
            while bytes_remaining:
                chunk_size = min(65536, bytes_remaining)
                cfile.write(fileobj.read(chunk_size))
                bytes_remaining -= chunk_size
