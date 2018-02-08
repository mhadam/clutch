# Clutch

`clutch` is a [Python][python] library for controlling [Transmission][transmission].

`clutch` is compatible with both Python2 and Python3.

To install:

```
pip install transmission-clutch
```

To use:

```
>>> import clutch
```

`clutch` was designed to be a more lightweight and consistent [Transmission][transmission]
RPC library than what was currently available for [Python][python]. Instead of simply
using the keys/fields in the [Transmission RPC spec][transmission-rpc] which have a mix of
dashed separated words and mixed case words, `clutch` tries to convert all
keys to be more Pythonic: underscore separated words. This conversion is
done so that it is still possible to specify the fields/argument specified in the [Transmission RPC spec][transmission-rpc], but if you do so your mileage may vary *(probably want to
avoid it)*.

`clutch` is designed to work with all versions of [Transmission][transmission], but for
renamed fields before and after Transmission version 1.60 ([RPC v5][rpcv5]) you
must specify the correct argument names (no automatic renames).

To use `clutch` to control a default `transmission-daemon` on
`localhost`:

```
>>> client = clutch.Client()
>>> client.list()
```

which produces a list of dictionaries with the torrent information (keys are
the fields: client.list_fields), and is synonymous to calling

```
>>> client.torrent.get(client.list_fields)
```

To use different connection information:

- complete path
```
  >>> client = clutch.Client(address="https://host:port/path")
```

- default URL, but port change to 8080
```
  >>> client = clutch.Client(port=8080)
```

- default URL, but different host
```
  >>> client = clutch.Client(host="github.com")
```

- default URL, but use a username and password
```
  >>> client = clutch.Client(username='username', password='password')
```

`clutch`'s RPC methods are namespaced into four sections:


[Client][client]:

- port_test -- return if transmission port is open.
- blocklist_update -- update block list and return block list size.
- *list* (`torrent.get` helper) -- list basic torrent info for all torrents.

[Client.queue][queue]:

- move_bottom -- move torrent to bottom of the queue.
- move_down -- move torrent down in the queue.
- move_top -- move torrent to the top of the queue.
- move_up -- move torrent up in the queue.

[Client.session][session]:

- close -- shutdown the Transmission daemon.
- get -- get session properties.
- set -- set session properties.
- stats -- get session statistics.

[Client.torrent][torrent]:

- add -- add a new torrent.
- get -- get torrent properties.
- *files* (`torrent.get` helper) -- get file information for one or more torrents.
- *percent_done* (`torrent.get` helper) -- get torrent percent done for one or more torrents.
- remove -- remove a torrent from transmission and optionally delete the data.
- set -- set torrent properties.
- set_location -- set/move torrent location.

[client]: https://github.com/mhadam/clutch/blob/master/clutch.py#L683
[queue]: https://github.com/mhadam/clutch/blob/master/clutch.py#L342
[session]: https://github.com/mhadam/clutch/blob/master/clutch.py#L349
[torrent]: https://github.com/mhadam/clutch/blob/master/clutch.py#L417

[python]: http://python.org/
[transmission]: http://www.transmissionbt.com/
[transmission-rpc]: https://trac.transmissionbt.com/browser/trunk/extras/rpc-spec.txt
[rpcv5]: https://trac.transmissionbt.com/browser/trunk/extras/rpc-spec.txt#L593
