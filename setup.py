#!/usr/bin/env python
# coding: utf-8

import os
from pathlib import Path

import setuptools

PYPI_PACKAGE_NAME = 'mtrayapp'
MAIN_PACKAGE_NAME = 'mtrayapp'
PACKAGE_URL = 'https://github.com/melianmiko/python-mtrayapp'
AUTHOR = u"Moses Palmér, melianmiko's mod"
# AUTHOR_EMAIL = 'moses.palmer@gmail.com'
AUTHOR_EMAIL = "melianmiko@yandex.ru"
VERSION = "1.0.1"

#: The runtime requirements
DEPENDENCIES = [
    'Pillow',
    'six'
]

#: Packages requires for different environments
EXTRA_PACKAGES = {
    ':sys_platform == "darwin"': [
        'pyobjc-framework-Quartz >=7.0'],
    ':sys_platform == "linux"': [
        'python-xlib >=0.17']}

this_directory = Path(__file__).parent
README = (this_directory / "README.md").read_text()

setuptools.setup(
    name=PYPI_PACKAGE_NAME,
    version=VERSION,
    description="Modification of Moses Palmér's pystray lib with some extra features",

    long_description=README,
    long_description_content_type='text/markdown',

    install_requires=DEPENDENCIES,
    extras_require=EXTRA_PACKAGES,

    author=AUTHOR,
    author_email=AUTHOR_EMAIL,

    url=PACKAGE_URL,

    packages=setuptools.find_packages(
        os.path.join(os.path.dirname(__file__), 'lib')
    ),
    package_dir={'': 'lib'},
    zip_safe=True,

    license='LGPLv3',
    keywords='system tray icon, systray icon',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 '
        '(LGPLv3)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows NT/2000',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'])
