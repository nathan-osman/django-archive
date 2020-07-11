from tarfile import TarInfo, TarFile


class TarballArchiver:
    """
    Archiver for creating tarballs (compressed and uncompressed)
    """

    UNCOMPRESSED = 'tar'
    GZ = 'gz'
    BZ2 = 'bz2'
    XZ = 'xz'

    @classmethod
    def get_extension(cls, fmt):
        """
        Determine the correct file extension for the archive
        """
        return fmt if fmt == cls.UNCOMPRESSED else 'tar.{}'.format(fmt)

    def __init__(self, fileobj, fmt):
        self._fileobj = fileobj
        self._fmt = fmt

    def __enter__(self):
        # pylint: disable=attribute-defined-outside-init
        self._tarfile = TarFile.open(
            mode='w:{}'.format(self._fmt),
            fileobj=self._fileobj,
        )

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._tarfile.close()

    def add(self, filename, size, fileobj):
        """
        Add the provided file to the archive
        """
        tarinfo = TarInfo(filename)
        tarinfo.size = size
        self._tarfile.addfile(tarinfo, fileobj)
