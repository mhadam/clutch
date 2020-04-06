from json import loads


def test_torrent_add_filename(client):
    file = "some_filename"
    try:
        client.torrent.add({"filename": file, "priority_low": []})
    except Exception as e:
        pass

    request_data = loads(client._connection.session.post.call_args.kwargs["data"])
    assert request_data["method"] == "torrent-add"
    assert request_data["arguments"] == {"filename": file, "priority-low": []}


def test_torrent_add_metainfo(client):
    metainfo = "some_metainfo"
    try:
        client.torrent.add({"metainfo": metainfo})
    except Exception:
        pass

    request_data = loads(client._connection.session.post.call_args.kwargs["data"])
    assert request_data["method"] == "torrent-add"
    assert request_data["arguments"] == {"metainfo": metainfo}
