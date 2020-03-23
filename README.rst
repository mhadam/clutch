Clutch
--------

.. image:: https://readthedocs.org/projects/clutch/badge/?version=latest
    :target: https://clutch.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/transmission-clutch.svg?style=flat-square
    :target: https://pypi.org/project/transmission-clutch

.. image:: https://img.shields.io/pypi/pyversions/transmission-clutch.svg?style=flat-square
    :target: https://pypi.org/project/transmission-clutch

.. image:: https://img.shields.io/badge/license-BSD-blue.svg?style=flat-square
    :target: https://en.wikipedia.org/wiki/BSD_License

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black

Quick start
===========

Install the package:

::

$ pip install transmission-clutch

Running the client is as easy as:

::

>>> from clutch.client import Client
>>> client = Client(address="http://localhost:9091/transmission")

If you find the client isn't connecting, make sure you're entering the address correctly. Reference `urllib.parse.urlparse`_ for parsing rules.

.. _urllib.parse.urlparse: https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse

RPC methods are separated into groups: torrent, session, queue and misc.

Methods are called by first specifying a group:

::

>>> client.torrent.add(...)
