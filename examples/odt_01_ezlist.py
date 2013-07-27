#!/usr/bin/env python
#coding:utf-8
# Purpose: create a simple list
# Created: 18.01.2011
# Copyright (C) 2011, Manfred Moitzi
# License: MIT
from __future__ import unicode_literals, print_function, division
__author__ = "mozman <mozman@gmx.at>"

import ezodf2

name = 'simple_list_document.odt'
odt = ezodf2.newdoc(doctype=name[-3:], filename=name)
content = odt.body
content.append(ezodf2.Heading("A Simple List"))
content.append(ezodf2.ezlist(['Point 1', 'Point 2', 'Point 3']))
odt.save()
