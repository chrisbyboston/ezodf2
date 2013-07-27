#!/usr/bin/env python
#coding:utf-8
# Purpose: Python Package for easy reading, writing and modifying of
#          OpenDocumentFormat files.
# Created: 27.12.2010
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
from __future__ import unicode_literals, print_function, division
__author__ = "mozman <mozman@gmx.at>"

version = (0, 2, 10)
VERSION = '%d.%d.%d' % version

from .document import opendoc, newdoc

# register classes by import
from .whitespaces import LineBreak, Tabulator, Spaces, SoftPageBreak
from .text import Span, Paragraph, Heading, Section, Hyperlink
from .text import List, ListHeader, ListItem, NumberedParagraph
from .table import Table
from .cells import Cell
from .conf import config

Sheet = Table

def ezlist(items, header="", style_name=""):
    """ Create a simple list.

    :param iterable items: iterable which yields strings
    :param str header: prepending list header
    :param str style_name: name of the associated list style
    :returns: ezodf2.text.List object
    """
    slist = List(style_name=style_name)
    if header:
        slist.header = ListHeader(header)
    for item in items:
        slist.append(ListItem(item))
    return slist
