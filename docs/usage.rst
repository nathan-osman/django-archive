Usage
=====

Interacting with Django Archive is done through a set of management commands.

Creating an Archive
-------------------

To create an archive, use the ``archive`` management command::

 python manage.py archive

This will create a compressed archive in the current directory containing
a single fixture in JSON format and all uploaded media.
