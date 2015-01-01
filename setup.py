from distutils.core import setup

setup(
    name='django_archive',
    version='0.1.2',
    description='Management command for creating compressed archives of DB tables and uploaded media',
    author='Nathan Osman',
    author_email='nathan@quickmediasolutions.com',
    url='https://github.com/nathan-osman/django-archive',
    license='MIT',
    packages=[
        'django_archive',
        'django_archive.management',
        'django_archive.management.commands',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ],
)
