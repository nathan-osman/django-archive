from tarfile import TarInfo, TarFile

from .registry import registry


class TarballArchiver:
    """
    Archiver for creating tarballs (compressed and uncompressed)
    """

    UNCOMPRESSED = 'tar'
    GZ = 'gz'
    BZ2 = 'bz2'
    XZ = 'xz'

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


registry.add(
    TarballArchiver.UNCOMPRESSED,
    TarballArchiver,
    "Tarball (.tar)",
    ('tar',),
)

registry.add(
    TarballArchiver.GZ,
    TarballArchiver,
    "gzip-compressed Tarball (.tar.gz)",
    ('tar.gz', 'tgz'),
)

registry.add(
    TarballArchiver.BZ2,
    TarballArchiver,
    "bzip2-compressed Tarball (.tar.bz2)",
    ('tar.bz2', 'tbz2'),
)

registry.add(
    TarballArchiver.XZ,
    TarballArchiver,
    "xz-compressed Tarball (.tar.xz)",
    ('tar.xz', 'txz'),
)
