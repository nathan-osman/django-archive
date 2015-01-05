Settings
========

Django Archive provides a number of settings that can be used to customize its
behavior. These settings are set on a per-project basis in ``settings.py``.

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
