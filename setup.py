#!/usr/bin/env python
import os
import re
from distutils.core import setup


def get_version(package):
    """
    Returns version of a package (`__version__` in `init.py`).
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.match("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('shortcuts')


setup(
    name='python-shortcuts',
    version=version,
    description='Python library to create and parse Siri Shortcuts',
    author='Alexander Akhmetov',
    author_email='me@aleks.sh',
    url='https://github.com/alexander-akhmetov/python-shortcuts',
    packages=[
        'shortcuts',
        'shortcuts.actions',
    ],
    entry_points={
        'console_scripts': [
            'shortcuts = shortcuts.cli:main',
        ],
    },
)
