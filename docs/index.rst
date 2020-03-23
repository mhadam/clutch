.. meta::
   :description: Transmission RPC library used to control the Transmission BitTorrent client.

.. title:: Transmission RPC Library: Clutch

Clutch - Transmission RPC for Python
====================================

Version |release|.

.. image:: https://img.shields.io/pypi/v/transmission-clutch.svg?style=flat-square
    :target: https://pypi.org/project/transmission-clutch

.. image:: https://img.shields.io/pypi/pyversions/transmission-clutch.svg?style=flat-square
    :target: https://pypi.org/project/transmission-clutch

.. image:: https://img.shields.io/badge/license-BSD-blue.svg?style=flat-square
    :target: https://en.wikipedia.org/wiki/BSD_License

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black

-----

.. toctree::
    :hidden:
    :maxdepth: 2
    :caption: Contents:

    intro
    server_config
    commands
    modules

Clutch is an open-source Python library for communicating over RPC_ with the `Transmission BitTorrent client`_.

It's handy for doing things like:

* automating work when managing torrents

* user interfaces and clients

* collecting torrent stats

Installation
------------

Pip
***
.. code-block:: console

    $ pip install transmission-clutch

Poetry
******
.. code-block:: console

    $ poetry add transmission-clutch

Get started
-------------

Import the package and make a client:

.. code-block:: python

    from clutch.client import Client
    client = Client(address="http://localhost:9091/transmission")

Now issue a command to Transmission:

.. code-block:: python

    >>> client.torrent.accessor(fields=['id', 'files'], ids=[1])
    Response(result='success', arguments={'torrents': [{'files': [{'bytes_completed': 1053440, 'length': 1053440, 'name': 'little_women/little_women.txt'}], 'id': 1}]}, tag=None)
.. _RPC: https://en.wikipedia.org/wiki/Remote_procedure_call
.. _`Transmission BitTorrent client`: https://transmissionbt.com
