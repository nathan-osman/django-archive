Settings
========

Django Archive provides a number of settings that can be used to customize its
behavior. These settings are optional, but may be modified on a per-project
basis in the project's ``settings.py``.

.. attribute:: ARCHIVE_DIRECTORY

    :default: *empty*

    Path to a directory where the archives will be stored. The default behavior
    is to create the archive in the current directory.

.. attribute:: ARCHIVE_FILENAME

    :default: ``'%Y-%m-%d--%H-%M-%S'``

    String passed to ``strftime()`` to determine the filename of the archive
    that will be generated.

.. attribute:: ARCHIVE_FORMAT

    :default: ``django_archive.archivers.TARBALL_BZ2``

    Format used for creating the compressed archive. The options currently
    available include:

    - ``django_archive.archivers.TARBALL``
    - ``django_archive.archivers.TARBALL_GZ``
    - ``django_archive.archivers.TARBALL_BZ2``
    - ``django_archive.archivers.TARBALL_XZ``
    - ``django_archive.archivers.ZIP``

    The predefined constants enable you to easily specify the archive format in
    your ``settings.py``:

    .. code-block:: python

        from django_archive import archivers
        ARCHIVE_FORMAT = archivers.ZIP

.. attribute:: ARCHIVE_EXCLUDE

    :default:

    ::

        (
            'contenttypes.ContentType',
            'sessions.Session',
            'auth.Permission',
        )

    List of models to exclude from the archive. By default, this includes
    session data and models that are automatically populated.
