Commands
========

Transmission RPC specifies a variety of methods to call.

In Clutch, those methods are implemented on :class:`~clutch.client.Client`.

Methods are organized into groups: :attr:`~clutch.client.Client.torrent`, :attr:`~clutch.client.Client.session`, :attr:`~clutch.client.Client.queue`, :attr:`~clutch.client.Client.misc`.

Torrent
-------
All torrent methods are found in :class:`~clutch.method.group.torrent.TorrentMethods`.

Session
-------
All session methods are found in :class:`~clutch.method.group.session.SessionMethods`.


Queue
-----
All queue methods are found in :class:`~clutch.method.group.queue.QueueMethods`.


Misc
----
All misc methods are found in :class:`~clutch.method.group.misc.MiscellaneousMethods`.
