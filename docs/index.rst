.. ezodf2 documentation master file, created by
   sphinx-quickstart on Thu Dec 30 16:01:08 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ezodf2's documentation!
=================================

**ezodf2** is a Python package to create new or open existing OpenDocumentFormat
files to extract, add, modify or delete document data. Supported python versions
are CPython 2.7 and CPython 3.2+, because the `lxml` package is needed, PyPy
support isn't possible at this time (01.01.2012).

To open an existing document, just use the :func:`ezodf2.opendoc` function::

    doc = ezodf2.opendoc('documentname.ext')

You don't have to care about the document type at the open function, to check
the type of the document, use the :attr:`~document.PackagedDocument.doctype` or
the :attr:`~document.PackagedDocument.mimetype` attribute::

    if doc.doctype == 'odt':
        pass
        # this is a text document
        # and so on for 'ods', 'odg' or 'odp'

To change the meta data of the document use the :attr:`~document.PackagedDocument.meta`
attribute, which is an instance of the :class:`meta.Meta` class::

   document_title = doc.meta['title']
   # or set meta attributes
   doc.meta['description'] = 'set a new description'

And save the modified document with the same filename as opened, a backup of
the original file will be created (if not disabled)::

   doc.save()

or save it with a new name::

   doc.saveas('newname.ext')

Contents
--------

.. toctree::
   :maxdepth: 2

   intro.rst

   docmanagement.rst
   document.rst
   meta.rst
   styles.rst
   textdocument.rst
   spreadsheetdocument.rst
   tableobjects.rst
   graphicsdocument.rst
   presentationdocument.rst
   howtos.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

