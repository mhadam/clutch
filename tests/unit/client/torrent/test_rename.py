from json import loads


def test_torrent_rename(client):
    path = "some_path"
    name = "some_name"
    try:
        client.torrent.rename(ids=[1, 2], path=path, name=name)
    except Exception as e:
        pass

    request_data = loads(client._connection.session.post.call_args.kwargs["data"])
    assert request_data["method"] == "torrent-rename-path"
    assert request_data["arguments"] == {"ids": [1, 2], "name": name, "path": path}
