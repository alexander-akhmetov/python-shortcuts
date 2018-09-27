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


with open('README.md', 'r') as f:
    readme = f.read()


setup(
    name='shortcuts',
    version=version,
    description='Python library to create and parse Siri Shortcuts',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Alexander Akhmetov',
    author_email='me@aleks.sh',
    url='https://github.com/alexander-akhmetov/python-shortcuts',
    python_requires="~=3.6",
    packages=[
        'shortcuts',
        'shortcuts.actions',
    ],
    install_requires=[
        'toml',
    ],
    entry_points={
        'console_scripts': [
            'shortcuts = shortcuts.cli:main',
        ],
    },
)
