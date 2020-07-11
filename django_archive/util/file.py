"""
Utility class for working with temporary files
"""

import os

from contextlib import contextmanager
from tempfile import mkstemp


class MixedModeTemporaryFile:
    """
    Temporary file that can be opened multiple times in different modes
    """

    def __init__(self):
        self._fd, self._filename = mkstemp()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        self.close()

    @contextmanager
    def open(self, mode):
        """
        Open the file in the specified mode
        """
        with os.fdopen(self._fd, mode, closefd=False) as fileobj:
            yield fileobj
        os.lseek(self._fd, 0, os.SEEK_SET)

    def close(self):
        """
        Close the temporary file (and delete it)
        """
        os.close(self._fd)
        os.unlink(self._filename)

    def size(self):
        """
        Return the size of the file
        """
        return os.stat(self._fd).st_size
