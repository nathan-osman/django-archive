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

This will create a compressed archive in the current directory containing a backup of the database tables and uploaded media. The command will take care of discovering all of the models in your project and finding fields that point to uploaded files.

### Settings

Although the default settings are sufficient for most simple projects, Django Archive provides a few settings that allow further customization of its behavior.

| Setting            | Default                     | Description |
|--------------------|-----------------------------|-------------|
| `ARCHIVE_FILENAME` | `%Y-%m-%d-%H-%M-%S.tar.bz2` | String passed to `strftime()` to determine the filename of the archive |
| `ARCHIVE_EXCLUDE`  | `('contenttypes.ContentType', 'sessions.Session','auth.Permission')` | List of models to exclude from the archive |

### Planned Features

The following features are planned for future releases:

* Command for restoring directly from an archive
* reST documentation for the package
* Comprehensive test suite
