Examples
--------

Create a client
===============
.. code-block:: python

    client = Client()

List all fields of current torrents
===================================

.. code-block:: python

    response: Response[TorrentAccessorResponse] = client.torrent.accessor(all_fields=True)
    torrents: Sequence[TorrentAccessorObject] = response.arguments.torrents
    print(torrents[0].dict(exclude_none=True))

Get specific fields of torrents
===============================

.. code-block:: python

    fields: Set[TorrentAccessorField] = {"id", "status", "name"}
    response: Response[TorrentAccessorResponse] = client.torrent.accessor(fields)
    torrents: Sequence[TorrentAccessorObject] = response.arguments.torrents
    torrent = torrents[0]
    torrent_id, torrent_status, torrent_name = torrent.id, torrent.status, torrent.name

Remove torrents
===============

.. code-block:: python

    response: Response[TorrentAccessorResponse] = client.torrent.remove(
        torrent_id, delete_local_data=False
    )

Add torrents
===============

.. code-block:: python

    arguments: TorrentAddArguments = {
        "filename": "/path/to/file",
        "paused": True,
    }
    response: Response[TorrentAdd] = client.torrent.add(arguments)
