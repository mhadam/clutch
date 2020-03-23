Clutch
--------

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
