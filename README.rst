Sphinx-doc external links
=========================

Install
-------

.. code-block:: bash

   $ pip install sphinx_links

Edit your Sphinx's ``conf.py``
------------------------------

.. code-block:: python

   links_collection = {
      'ITCase': 'http://itcase.pro',
      'YoPhone': 'https://yotaphone.com',
      'Pyramid': 'http://www.pylonsproject.org',
   }

   extensions = ['sphinx_links', ]

Usage
-----

::

   :l:`Pyramid` framework.
   :l:`YoPhone` eink with GSM.
   :l:`ITCase` LLC.
