Settings
========

Django Archive provides a number of settings that can be used to customize its
behavior. These settings are optional, but may be modified on a per-project
basis in the project's ``settings.py``.

``ARCHIVE_DIRECTORY``
---------------------

**Default:** *empty*

Directory where the archive will be stored. The default behavior is to create the
archive in the current directory.

``ARCHIVE_FILENAME``
--------------------

**Default:** ``'%Y-%m-%d--%H-%M-%S'``

String passed to ``strftime()`` to determine the filename of the archive.

``ARCHIVE_FORMAT``
------------------

**Default:** ``'bz2'``

Format used for creating the compressed archive. The two options currently
available include:

- ``'bz2'``
- ``'gz'``

``ARCHIVE_EXCLUDE``
-------------------

**Default:**

::

  (
      'contenttypes.ContentType',
      'sessions.Session',
      'auth.Permission',
  )

List of models to exclude from the archive.
