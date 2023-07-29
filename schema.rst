README
======

Top-level Schemas
-----------------

-  `Project Definition <./schema.md>`__ – ``-``

Other Schemas
-------------

Objects
~~~~~~~

-  `Document
   Include <./schema-properties-document-includes-document-include.md>`__
   – ``undefined#/properties/includes/items``

Arrays
~~~~~~

-  `Document Includes <./schema-properties-document-includes.md>`__ –
   ``undefined#/properties/includes``

Version Note
------------

The schemas linked above follow the JSON Schema Spec version:
``https://json-schema.org/draft/2020-12`` # Project Definition Schema

.. code:: txt

   undefined

Document Slammer Project Definition Version 0.1

.. list-table::
   :widths: 8 4 6 5 7 9 8 25
   :header-rows: 1

   - 

      - Abstract
      - Extensible
      - Status
      - Identifiable
      - Custom Properties
      - Additional Properties
      - Access Restrictions
      - Defined In
   - 

      - Can be instantiated
      - No
      - Unknown status
      - No
      - Forbidden
      - Forbidden
      - none
      - `schema.json <../../out/schema.json>`__

Project Definition Type
-----------------------

``object`` (`Project Definition <schema.md>`__)

Project Definition Properties
=============================

.. list-table::
   :widths: 13 4 4 7 44
   :header-rows: 1

   - 

      - Property
      - Type
      - Required
      - Nullable
      - Defined by
   - 

      - `title <#title>`__
      - ``string``
      - Required
      - cannot be null
      - `Project Definition <schema-properties-title.md>`__
   - 

      - `number_font <#number_font>`__
      - ``string``
      - Optional
      - cannot be null
      - `Project Definition <schema-properties-numbering-font.md>`__
   - 

      - `includes <#includes>`__
      - ``array``
      - Required
      - cannot be null
      - `Project Definition <schema-properties-document-includes.md>`__

title
-----

The overall title of the document.

``title``

-  is required

-  Type: ``string`` (`Title <schema-properties-title.md>`__)

-  cannot be null

-  defined in: `Project Definition <schema-properties-title.md>`__

title Type
~~~~~~~~~~

``string`` (`Title <schema-properties-title.md>`__)

number_font
-----------

Not yet implemented. An optional override for the font to use for page
numbering. Defaults to Helvetica, which should be universally available.

``number_font``

-  is optional

-  Type: ``string`` (`Numbering
   Font <schema-properties-numbering-font.md>`__)

-  cannot be null

-  defined in: `Project
   Definition <schema-properties-numbering-font.md>`__

number_font Type
~~~~~~~~~~~~~~~~

``string`` (`Numbering Font <schema-properties-numbering-font.md>`__)

includes
--------

Provides a sequence of documents and their corresponding table of
contents heading for inclusion.

``includes``

-  is required

-  Type: ``object[]`` (`Document
   Include <schema-properties-document-includes-document-include.md>`__)

-  cannot be null

-  defined in: `Project
   Definition <schema-properties-document-includes.md>`__

includes Type
~~~~~~~~~~~~~

``object[]`` (`Document
Include <schema-properties-document-includes-document-include.md>`__) #
Document Include Schema

.. code:: txt

   undefined#/properties/includes/items

A document alongside its corresponding Table of Contents heading for
inclusion into the booklet.

.. list-table::
   :widths: 8 4 6 5 7 9 8 25
   :header-rows: 1

   - 

      - Abstract
      - Extensible
      - Status
      - Identifiable
      - Custom Properties
      - Additional Properties
      - Access Restrictions
      - Defined In
   - 

      - Can be instantiated
      - No
      - Unknown status
      - No
      - Forbidden
      - Forbidden
      - none
      - `schema.json\* <../../out/schema.json>`__

items Type
----------

``object`` (`Document
Include <schema-properties-document-includes-document-include.md>`__)

items Properties
================

.. list-table::
   :widths: 7 3 3 5 55
   :header-rows: 1

   - 

      - Property
      - Type
      - Required
      - Nullable
      - Defined by
   - 

      - `path <#path>`__
      - ``string``
      - Required
      - cannot be null
      - `Project
         Definition <schema-properties-document-includes-document-include-properties-path.md>`__
   - 

      - `heading <#heading>`__
      - ``string``
      - Required
      - cannot be null
      - `Project
         Definition <schema-properties-document-includes-document-include-properties-heading.md>`__

path
----

Relative path from the document root to the document to include.

``path``

-  is required

-  Type: ``string``

-  cannot be null

-  defined in: `Project
   Definition <schema-properties-document-includes-document-include-properties-path.md>`__

path Type
~~~~~~~~~

``string``

path Constraints
~~~~~~~~~~~~~~~~

**minimum length**: the minimum number of characters for this string is:
``1``

heading
-------

The heading to display within the Table of Contents for this document.

``heading``

-  is required

-  Type: ``string``

-  cannot be null

-  defined in: `Project
   Definition <schema-properties-document-includes-document-include-properties-heading.md>`__

heading Type
~~~~~~~~~~~~

``string``

heading Constraints
~~~~~~~~~~~~~~~~~~~

**minimum length**: the minimum number of characters for this string is:
``1`` # Untitled string in Project Definition Schema

.. code:: txt

   undefined#/properties/includes/items/properties/heading

The heading to display within the Table of Contents for this document.

.. list-table::
   :widths: 7 4 5 9 7 8 7 24
   :header-rows: 1

   - 

      - Abstract
      - Extensible
      - Status
      - Identifiable
      - Custom Properties
      - Additional Properties
      - Access Restrictions
      - Defined In
   - 

      - Can be instantiated
      - No
      - Unknown status
      - Unknown identifiability
      - Forbidden
      - Allowed
      - none
      - `schema.json\* <../../out/schema.json>`__

.. _heading-type-1:

heading Type
------------

``string``

.. _heading-constraints-1:

heading Constraints
-------------------

**minimum length**: the minimum number of characters for this string is:
``1`` # Untitled string in Project Definition Schema

.. code:: txt

   undefined#/properties/includes/items/properties/path

Relative path from the document root to the document to include.

.. list-table::
   :widths: 7 4 5 9 7 8 7 24
   :header-rows: 1

   - 

      - Abstract
      - Extensible
      - Status
      - Identifiable
      - Custom Properties
      - Additional Properties
      - Access Restrictions
      - Defined In
   - 

      - Can be instantiated
      - No
      - Unknown status
      - Unknown identifiability
      - Forbidden
      - Allowed
      - none
      - `schema.json\* <../../out/schema.json>`__

.. _path-type-1:

path Type
---------

``string``

.. _path-constraints-1:

path Constraints
----------------

**minimum length**: the minimum number of characters for this string is:
``1`` # Document Includes Schema

.. code:: txt

   undefined#/properties/includes

Provides a sequence of documents and their corresponding table of
contents heading for inclusion.

.. list-table::
   :widths: 7 4 5 9 7 8 7 24
   :header-rows: 1

   - 

      - Abstract
      - Extensible
      - Status
      - Identifiable
      - Custom Properties
      - Additional Properties
      - Access Restrictions
      - Defined In
   - 

      - Can be instantiated
      - No
      - Unknown status
      - Unknown identifiability
      - Forbidden
      - Allowed
      - none
      - `schema.json\* <../../out/schema.json>`__

.. _includes-type-1:

includes Type
-------------

``object[]`` (`Document
Include <schema-properties-document-includes-document-include.md>`__) #
Untitled object in Project Definition Schema

.. code:: txt

   undefined#/properties/includes/items

.. list-table::
   :widths: 8 4 6 5 7 9 8 25
   :header-rows: 1

   - 

      - Abstract
      - Extensible
      - Status
      - Identifiable
      - Custom Properties
      - Additional Properties
      - Access Restrictions
      - Defined In
   - 

      - Can be instantiated
      - No
      - Unknown status
      - No
      - Forbidden
      - Forbidden
      - none
      - `schema.json\* <../../out/schema.json>`__

.. _items-type-1:

items Type
----------

``object`` (`Details <schema-properties-includes-items.md>`__)

.. _items-properties-1:

items Properties
================

.. list-table::
   :widths: 7 3 3 6 53
   :header-rows: 1

   - 

      - Property
      - Type
      - Required
      - Nullable
      - Defined by
   - 

      - `path <#path>`__
      - ``string``
      - Required
      - cannot be null
      - `Project
         Definition <schema-properties-includes-items-properties-path.md>`__
   - 

      - `heading <#heading>`__
      - ``string``
      - Required
      - cannot be null
      - `Project
         Definition <schema-properties-includes-items-properties-heading.md>`__

.. _path-1:

path
----

Relative path from the document root to the document to include.

``path``

-  is required

-  Type: ``string``

-  cannot be null

-  defined in: `Project
   Definition <schema-properties-includes-items-properties-path.md>`__

.. _path-type-2:

path Type
~~~~~~~~~

``string``

.. _path-constraints-2:

path Constraints
~~~~~~~~~~~~~~~~

**minimum length**: the minimum number of characters for this string is:
``1``

.. _heading-1:

heading
-------

The heading to display within the Table of Contents for this document.

``heading``

-  is required

-  Type: ``string``

-  cannot be null

-  defined in: `Project
   Definition <schema-properties-includes-items-properties-heading.md>`__

.. _heading-type-2:

heading Type
~~~~~~~~~~~~

``string``

.. _heading-constraints-2:

heading Constraints
~~~~~~~~~~~~~~~~~~~

**minimum length**: the minimum number of characters for this string is:
``1`` # Untitled string in Project Definition Schema

.. code:: txt

   undefined#/properties/includes/items/properties/heading

The heading to display within the Table of Contents for this document.

.. list-table::
   :widths: 7 4 5 9 7 8 7 24
   :header-rows: 1

   - 

      - Abstract
      - Extensible
      - Status
      - Identifiable
      - Custom Properties
      - Additional Properties
      - Access Restrictions
      - Defined In
   - 

      - Can be instantiated
      - No
      - Unknown status
      - Unknown identifiability
      - Forbidden
      - Allowed
      - none
      - `schema.json\* <../../out/schema.json>`__

.. _heading-type-3:

heading Type
------------

``string``

.. _heading-constraints-3:

heading Constraints
-------------------

**minimum length**: the minimum number of characters for this string is:
``1`` # Untitled string in Project Definition Schema

.. code:: txt

   undefined#/properties/includes/items/properties/path

Relative path from the document root to the document to include.

.. list-table::
   :widths: 7 4 5 9 7 8 7 24
   :header-rows: 1

   - 

      - Abstract
      - Extensible
      - Status
      - Identifiable
      - Custom Properties
      - Additional Properties
      - Access Restrictions
      - Defined In
   - 

      - Can be instantiated
      - No
      - Unknown status
      - Unknown identifiability
      - Forbidden
      - Allowed
      - none
      - `schema.json\* <../../out/schema.json>`__

.. _path-type-3:

path Type
---------

``string``

.. _path-constraints-3:

path Constraints
----------------

**minimum length**: the minimum number of characters for this string is:
``1`` # Untitled array in Project Definition Schema

.. code:: txt

   undefined#/properties/includes

Provides a document and its corresponding table of contents heading for
inclusion.

.. list-table::
   :widths: 7 4 5 9 7 8 7 24
   :header-rows: 1

   - 

      - Abstract
      - Extensible
      - Status
      - Identifiable
      - Custom Properties
      - Additional Properties
      - Access Restrictions
      - Defined In
   - 

      - Can be instantiated
      - No
      - Unknown status
      - Unknown identifiability
      - Forbidden
      - Allowed
      - none
      - `schema.json\* <../../out/schema.json>`__

.. _includes-type-2:

includes Type
-------------

``object[]`` (`Details <schema-properties-includes-items.md>`__) #
Untitled string in Project Definition Schema

.. code:: txt

   undefined#/properties/number_font

Not yet implemented. An optional override for the font to use for page
numbering. Defaults to Helvetica, which should be universally available.

.. list-table::
   :widths: 7 4 5 9 7 8 7 24
   :header-rows: 1

   - 

      - Abstract
      - Extensible
      - Status
      - Identifiable
      - Custom Properties
      - Additional Properties
      - Access Restrictions
      - Defined In
   - 

      - Can be instantiated
      - No
      - Unknown status
      - Unknown identifiability
      - Forbidden
      - Allowed
      - none
      - `schema.json\* <../../out/schema.json>`__

.. _number_font-type-1:

number_font Type
----------------

``string`` # Numbering Font Schema

.. code:: txt

   undefined#/properties/number_font

Not yet implemented. An optional override for the font to use for page
numbering. Defaults to Helvetica, which should be universally available.

.. list-table::
   :widths: 7 4 5 9 7 8 7 24
   :header-rows: 1

   - 

      - Abstract
      - Extensible
      - Status
      - Identifiable
      - Custom Properties
      - Additional Properties
      - Access Restrictions
      - Defined In
   - 

      - Can be instantiated
      - No
      - Unknown status
      - Unknown identifiability
      - Forbidden
      - Allowed
      - none
      - `schema.json\* <../../out/schema.json>`__

.. _number_font-type-2:

number_font Type
----------------

``string`` (`Numbering Font <schema-properties-numbering-font.md>`__) #
Title Schema

.. code:: txt

   undefined#/properties/title

The overall title of the document.

.. list-table::
   :widths: 7 4 5 9 7 8 7 24
   :header-rows: 1

   - 

      - Abstract
      - Extensible
      - Status
      - Identifiable
      - Custom Properties
      - Additional Properties
      - Access Restrictions
      - Defined In
   - 

      - Can be instantiated
      - No
      - Unknown status
      - Unknown identifiability
      - Forbidden
      - Allowed
      - none
      - `schema.json\* <../../out/schema.json>`__

.. _title-type-1:

title Type
----------

``string`` (`Title <schema-properties-title.md>`__)
