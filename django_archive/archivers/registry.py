from collections import namedtuple


class Registry:
    """
    A set of methods for finding and enumerating supported archivers
    """

    Format = namedtuple("Format", ('archiver', 'description', 'extensions'))

    def __init__(self):
        self._formats = {}

    def list(self):
        """
        Return a list of format IDs
        """
        return self._formats.keys()

    # pylint: disable=invalid-name,redefined-builtin
    def add(self, id, archiver, description, extensions):
        """
        Add a format to the registry
        """
        self._formats[id] = self.Format(archiver, description, extensions)

    # pylint: disable=invalid-name,redefined-builtin
    def get(self, id):
        """
        Retrieve a format by its ID
        """
        return self._formats[id]

    def find_by_extension(self, extension):
        """
        Find a format by its extension
        """
        for fmt in self._formats.values():
            for ext in fmt.extensions:
                if ext == extension:
                    return fmt
        raise KeyError("No archiver exists for '{}'".format(extension))


registry = Registry()
