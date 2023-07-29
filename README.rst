Document Slammer
----------------

Overview
========

Combines separate PDFs into a booklet format with page numbering and table of contents. Works well in conjunction with tools like pandoc to create printable reference guides comprising materials from disparate sources.

Requirements
============

* Python 3.10
* Poetry
* PDFLaTeX
* Poppler Utils
* awk

Installation
============

This is a poetry-managed project; you should be able to install it via:

.. code-block:: shell

    poetry self install

Usage
=====

In order to use this tool, you will need to create a configuration in a root directory you've chosen for your project. It also helps to organize your PDFs within your project's root directory.

Here is the recommended layout:

* Root Directory

  - ``doc.yaml``
  - ``documents``

    - ``doc-1.pdf``
    - ``doc-2.pdf``

And, given the above structure, here is a sample ``doc.yaml``. See `Schema <schema.rst>`_ for a full schema reference.

.. code-block:: yaml

   title: A Cool and Creative Title
   includes:
     - path: documents/doc-1.pdf
       heading: Some Reference Guide
     - path: documents/doc-2.pdf
       heading: Some blog somewhere


Now, sync the project:

.. code-block:: shell

    python -m document_slammer sync doc.yaml

And, finally, run ``make`` to build ``Booklet.pdf``.

Printing
========

Print the booklet with double sided printing on, binding on **Short Edge**. Most double sided printers will default to long-edge binding, which is not compatible.
