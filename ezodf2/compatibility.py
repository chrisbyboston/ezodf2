#!/usr/bin/env python
#coding:utf-8
# Purpose: compatibility layer
# Created: 01.01.12
# Copyright (C) 2012, Manfred Moitzi
# License: MIT
from __future__ import unicode_literals, print_function, division
__author__ = "mozman <mozman@gmx.at>"

import sys

PY3 = sys.version_info[0] > 2

if PY3:
    itermap=map
    tostr = str
    def is_string(value):
        return isinstance(value, str)

    def is_bytes(value):
        return isinstance(value, bytes)

    def tobytes(element):
        if isinstance(element, str):
            return element.encode('utf-8')
        elif isinstance(element, bytes):
            return element
        else:
            raise TypeError('Unsupported type: %s' % type(element))

    def bytes2unicode(bytes):
        return str(bytes, 'utf-8')

else: # PY2
    tostr=unicode
    def is_string(value):
        # TODO: ??? shouldn't be an instance of 'unicode' ???
        return isinstance(value, basestring)

    def is_bytes(value):
        return isinstance(value, str)

    def itermap(function, iterable):
        return iter(map(function, iterable))

    def tobytes(element):
        if isinstance(element, unicode):
            return element.encode('utf-8')
        elif isinstance(element, str):
            return element
        else:
            raise TypeError('Unsupported type: %s' % type(element))

    def bytes2unicode(bytes):
        return bytes.decode('utf-8')
