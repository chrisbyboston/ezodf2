Abstract
========

**ezodf2** is a Python package to create new or open existing OpenDocument
(ODF) files to extract, add, modify or delete document data.

a simple example::

    from ezodf2 import newdoc, Paragraph, Heading, Sheet

    odt = newdoc(doctype='odt', filename='text.odt')
    odt.body += Heading("Chapter 1")
    odt.body += Paragraph("This is a paragraph.")
    odt.save()

    ods = newdoc(doctype='ods', filename='spreadsheet.ods')
    sheet = Sheet('SHEET', size=(10, 10))
    ods.sheets += sheet
    sheet['A1'].set_value("cell with text")
    sheet['B2'].set_value(3.141592)
    sheet['C3'].set_value(100, currency='USD')
    sheet['D4'].formula = "of:=SUM([.B2];[.C3])"
    pi = sheet[1, 1].value
    ods.save()

for more examples see: /examples folder

Continuous Integration Status
=============================

[![Build Status](https://travis-ci.org/iwschris/ezodf2.png)](https://travis-ci.org/iwschris/ezodf2.png)


Dependencies
============

* lxml <http://codespeak.net/lxml/> for painless serialisation with prefix
  declaration (xlmns:prefix="global:namespace:specifier") in the root element.
  Declarations for unused prefixes are also possible.

The target platform is Python 2.7 and Python 3.2+.

Installation
============

with pip::

    pip install ezodf2

or from source::

    python setup.py install

Documentation
=============

http://packages.python.org/ezodf2

send feedback to chris@britecore.com

ezodf2 can be found on github at:

http://github.com/iwschris/ezodf2

History
=======
This package was originally created by Manfred Moitzi under the name ezodf (https://bitbucket.org/mozman/ezodf)
