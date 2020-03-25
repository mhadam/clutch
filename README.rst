Clutch
--------

.. image:: https://readthedocs.org/projects/clutch/badge/?version=latest
    :target: https://clutch.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/transmission-clutch.svg?style=flat-square
    :target: https://pypi.org/project/transmission-clutch

.. image:: https://img.shields.io/pypi/pyversions/transmission-clutch.svg?style=flat-square
    :target: https://pypi.org/project/transmission-clutch

.. image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
    :target: https://en.wikipedia.org/wiki/MIT_License

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black

Quick start
===========

Install the package:

.. code-block:: console

    $ pip install transmission-clutch

Make a client:

.. code-block:: python

    from clutch.client import Client
    client = Client()

If you find the client isn't connecting (an error will be raised), make sure you're entering the address correctly. Reference `urllib.parse.urlparse`_ for parsing rules.

You can specify Transmission's address when making the client:

.. code-block:: python

    client = Client(address="http://localhost:9091/transmission/rpc")

.. _urllib.parse.urlparse: https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse

RPC methods are separated into groups: torrent, session, queue and misc.

Methods are called by first specifying a group:

.. code-block:: python

    client.torrent.add(...)
