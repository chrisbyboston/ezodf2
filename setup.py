#!/usr/bin/env python
#coding:utf-8
# Author:  iwschris
# Purpose: setup
# Created: 2013-07-13
#
# The MIT License (MIT)

# Copyright (c) 2010 Manfred Moitzi
# Modified work Copyright 2013 Chris Reynolds

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return "File '%s' not found.\n" % fname

setup(
    name='ezodf2',
    version='0.2.9',
    url='http://github.com/iwschris/ezodf2',
    license='MIT',
    author='Chris Reynolds',
    author_email='chris@britecore.com',
    description='A Python package to create/manipulate OpenDocumentFormat files.',
    long_description=read('README.md')+'\n'+read('CHANGES'),
    packages=['ezodf2'],
    include_package_data=True,
    platforms='OS Independent',
    install_requires=['lxml'],
    keywords=['ODF', 'OpenDocumentFormat', 'OpenOffice', 'LibreOffice'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
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
