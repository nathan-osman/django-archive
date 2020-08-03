from .registry import registry
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
    (this method is deprecated in favor of the registry)
    """
    # pylint: disable=import-outside-toplevel
    from warnings import warn
    warn(
        "get_archiver() is deprecated; use the registry instead",
        DeprecationWarning,
        stacklevel=2,
    )
    return registry.get(fmt)
