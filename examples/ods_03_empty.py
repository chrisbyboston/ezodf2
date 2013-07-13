#!/usr/bin/env python
#coding:utf-8
# Purpose: empty spreadsheet
# Created: 26.01.2011
# Copyright (C) 2011, Manfred Moitzi
# License: GPLv3
from __future__ import unicode_literals, print_function, division
__author__ = "mozman <mozman@gmx.at>"

import ezodf2

ods = ezodf2.newdoc('ods', "empty_spreadsheet.ods")
for sheetname in ['SHEET1', 'SHEET2', 'SHEET3']:
    ods.sheets += ezodf2.Sheet(name=sheetname, size=(20, 10))

ods.save()
