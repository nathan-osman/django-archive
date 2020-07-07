from .tarball import TarballArchiver
from .zipfile import ZipArchiver


TARBALL = TarballArchiver.UNCOMPRESSED
TARBALL_GZ = TarballArchiver.GZ
TARBALL_BZ2 = TarballArchiver.BZ2
TARBALL_XZ = TarballArchiver.XZ
ZIP = 'zip'


def get_archiver(fmt):
    """
    Return the class corresponding with the provided archival format
    """
    if fmt in (TARBALL, TARBALL_GZ, TARBALL_BZ2, TARBALL_XZ):
        return TarballArchiver
    if fmt == ZIP:
        return ZipArchiver
    raise KeyError("Invalid format '{}' specified".format(fmt))
