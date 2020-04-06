from json import loads

from clutch.schema.user.method.torrent.action import TorrentActionMethod


def test_torrent_action(client):
    try:
        client.torrent.action(TorrentActionMethod.START_NOW, ids=[1, 2])
    except Exception:
        pass

    request_data = loads(client._connection.session.post.call_args.kwargs["data"])
    assert request_data["method"] == TorrentActionMethod.START_NOW.value
    assert request_data["arguments"] == {"ids": [1, 2]}
