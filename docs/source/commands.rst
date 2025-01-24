Commands
========

Transmission RPC specifies a variety of methods to call.

In Clutch, those methods are implemented on :class:`~clutch.client.Client`.

Groups
------

Client methods are organized into groups: :attr:`~clutch.client.Client.torrent`, :attr:`~clutch.client.Client.session`, :attr:`~clutch.client.Client.queue`, :attr:`~clutch.client.Client.misc`.

Torrent
.......
All torrent methods are found in :class:`~clutch.method.torrent.TorrentMethods`.

Session
.......
All session methods are found in :class:`~clutch.method.session.SessionMethods`.

Queue
.....
All queue methods are found in :class:`~clutch.method.queue.QueueMethods`.

Misc
....
All misc methods are found in :class:`~clutch.method.misc.MiscellaneousMethods`.

Responses
---------
Methods return a :class:`~clutch.network.rpc.message.Response` object that has three fields: ``result``, ``arguments`` and ``tag``.

The :class:`~clutch.network.rpc.message.Response` object and :attr:`~clutch.network.rpc.message.Response.arguments` field are both `pydantic models`_.

So they have some `useful methods for converting`_ into simple data formats like ``dict``:

.. code-block:: python

    model.dict(...)

Or a JSON string:

.. code-block:: python

    model.json(...)

To make a model with many fields more manageable, remove the clutter of empty fields using the option ``exclude_none``:

.. code-block:: python

    model.dict(exclude_none=True)

.. _pydantic models: https://pydantic-docs.helpmanual.io/usage/models/
.. _useful methods for converting: https://pydantic-docs.helpmanual.io/usage/exporting_models/
