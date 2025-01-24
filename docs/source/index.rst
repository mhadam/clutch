.. meta::
   :description: Transmission RPC library used to control the Transmission BitTorrent client.

.. title:: Transmission RPC Library: Clutch

Clutch - Transmission RPC for Python
====================================

Version |release|.

.. image:: https://img.shields.io/github/stars/mhadam/clutch?style=social
    :target: https://github.com/mhadam/clutch
    :alt: GitHub stars badge

.. image:: https://img.shields.io/pypi/v/transmission-clutch.svg
    :target: https://pypi.org/project/transmission-clutch
    :alt: PyPI badge

.. image:: https://img.shields.io/pypi/pyversions/transmission-clutch.svg
    :target: https://pypi.org/project/transmission-clutch
    :alt: PyPI versions badge

.. image:: https://img.shields.io/pypi/l/transmission-clutch.svg
    :target: https://en.wikipedia.org/wiki/MIT_License
    :alt: License badge

-----

.. toctree::
    :hidden:
    :maxdepth: 2
    :caption: Contents:

    intro
    examples
    server_config
    commands
    modules

Clutch is an open-source Python library for talking to the `Transmission BitTorrent client`_ over RPC_.

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

    from clutch import Client
    client = Client(address="http://localhost:9091/transmission/rpc")

Now issue a command to Transmission:

.. code-block:: python

    >>> client.torrent.accessor(fields=['id', 'files'], ids=[1]).dict(exclude_none=True)
    {'result': 'success', 'arguments': {'torrents': [{'files': [{'bytes_completed': 1053440, 'length': 1053440, 'name': 'little_women/little_women.txt'}], 'id': 1}]}}
    >>> client.torrent.accessor(fields=['id', 'files'], ids=[1]).json(exclude_none=True)
    '{"result": "success", "arguments": {"torrents": [{"files": [{"bytes_completed": 1053440, "length": 1053440, "name": "little_women/little_women.txt"}], "id": 1}]}}'

.. _RPC: https://en.wikipedia.org/wiki/Remote_procedure_call
.. _`Transmission BitTorrent client`: https://transmissionbt.com
