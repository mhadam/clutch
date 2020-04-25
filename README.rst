Clutch
------

.. image:: https://readthedocs.org/projects/clutch/badge/?version=latest
    :target: https://clutch.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation badge

.. image:: https://img.shields.io/pypi/v/transmission-clutch.svg
    :target: https://pypi.org/project/transmission-clutch
    :alt: PyPI badge

.. image:: https://img.shields.io/pypi/pyversions/transmission-clutch.svg
    :target: https://pypi.org/project/transmission-clutch
    :alt: PyPI versions badge

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
    :alt: Black formatter badge

.. image:: https://img.shields.io/pypi/l/transmission-clutch.svg
    :target: https://en.wikipedia.org/wiki/MIT_License
    :alt: License badge

.. image:: https://img.shields.io/pypi/dm/transmission-clutch.svg
    :target: https://pypistats.org/packages/transmission-clutch
    :alt: PyPI downloads badge

Documentation
=============

Found here: `<https://clutch.readthedocs.io>`_

Quick start
===========

Install the package:

.. code-block:: console

    $ pip install transmission-clutch

Make a client:

.. code-block:: python

    from clutch import Client
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
