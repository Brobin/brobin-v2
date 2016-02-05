==============
brobin.me
==============

This is the repo for my personal website: `brobin.me <http://brobin.me/>`_. Feel free to use it for your own site, play around with it etc.

---------------

|python| |django| |build|

---------------

----------
Quickstart
----------

Clone the repo and install the requirements

* Python 3.4
* Django 1.9
* mysqlclient 1.3.7

Django and mysqlclient can be installed via pip

.. code-block:: bash

    $ pip install django, mysqlclient

Then, copy the `test_settings.py` into `local_settings.py` and change them as desired.

.. code-block:: bash

    $ cp brobin/test_settings.py brobin/local_settings.py

Update the database, creat a user, and you're good to go!

.. code-block:: bash

    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver

-------
License
-------

**tl;dr**: You can use this, but I don't guarantee anything will work, and you must include the license.

.. code-block::

    The MIT License (MIT)

    Copyright (c) 2016 Tobin Brown

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.


.. |python| image:: https://img.shields.io/badge/Python-3.4-blue.svg?style=flat-square
    :target: http://python.org/
    :alt: Python 3.4

.. |django| image:: https://img.shields.io/badge/Django-1.9-orange.svg?style=flat-square
    :target: http://djangoproject.com/
    :alt: Django 1.9

.. |build| image:: https://img.shields.io/travis/Brobin/brobin.me.svg?style=flat-square
    :target: https://travis-ci.org/Brobin/brobin.me/
    :alt: Travis CI

