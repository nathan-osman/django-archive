from .tarball import TarballArchiver
from .zipfile import ZipArchiver


TARBALL = TarballArchiver.UNCOMPRESSED
TARBALL_GZ = TarballArchiver.GZ
TARBALL_BZ2 = TarballArchiver.BZ2
TARBALL_XZ = TarballArchiver.XZ
ZIP = 'zip'

FORMATS = (
    TARBALL,
    TARBALL_GZ,
    TARBALL_BZ2,
    TARBALL_XZ,
    ZIP,
)

FORMATS_DESC = {
    TARBALL: "Tarball (.tar)",
    TARBALL_GZ: "gzip-compressed Tarball (.tar.gz)",
    TARBALL_BZ2: "bzip2-compressed Tarball (.tar.bz2)",
    TARBALL_XZ: "xz-compressed Tarball (.tar.xz)",
    ZIP: "ZIP archive (.zip)",
}


def get_archiver(fmt):
    """
    Return the class corresponding with the provided archival format
    """
    if fmt in (TARBALL, TARBALL_GZ, TARBALL_BZ2, TARBALL_XZ):
        return TarballArchiver
    if fmt == ZIP:
        return ZipArchiver
    raise KeyError("Invalid format '{}' specified".format(fmt))
