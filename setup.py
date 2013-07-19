#!/usr/bin/env python
#coding:utf-8
# Author:  iwschris
# Purpose: setup
# Created: 2013-07-13
#
#    Copyright (C) 2010  Manfred Moitzi
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from distutils.core import setup

from ezodf2 import VERSION

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return "File '%s' not found.\n" % fname

setup(
    name='ezodf2',
    version=VERSION,
    url='http://github.com/iwschris/ezodf2',
    license='GPLv3',
    author='Chris Reynolds',
    author_email='chris@britecore.com',
    description='A Python package to create/manipulate OpenDocumentFormat files.',
    long_description=read('README.md')+'\n'+read('CHANGES'),
    packages=['ezodf2'],
    platforms='OS Independent',
    install_requires=['distribute',
                      'lxml'],
    keywords=['ODF', 'OpenDocumentFormat', 'OpenOffice', 'LibreOffice'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Office Suites",
    ]
)
