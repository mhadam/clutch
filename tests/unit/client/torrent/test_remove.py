from json import loads


def test_torrent_remove(client):
    try:
        client.torrent.remove(ids=[1, 2], delete_local_data=True)
    except Exception as e:
        pass

    request_data = loads(client._connection.session.post.call_args.kwargs["data"])
    assert request_data["method"] == "torrent-remove"
    assert request_data["arguments"] == {"ids": [1, 2], "delete-local-data": True}
