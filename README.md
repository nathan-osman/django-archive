## Django Archive

Django Archive provides a management command that will create a compressed archive of database tables and uploaded media.

### Requirements

The following minimum requirements must be met:

 - Python 2.7+ or Python 3.x
 - Django 1.7+

### Installation

Installing Django Archive is as easy as running:

    pip install django-archive

In order to add Django Archive to your project, add `'django_archive'` to the `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        # ...
        'django_archive',
    )

### Usage

Creating an archive is as simple as running the following management command:

    ./manage.py archive

This will create a compressed archive in the current directory containing a backup of the database tables and uploaded media.
