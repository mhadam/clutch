from json import loads


def test_torrent_move(client):
    location = "some_location"
    try:
        client.torrent.move(ids=[1, 2], location=location, move=True)
    except Exception as e:
        pass

    request_data = loads(client._connection.session.post.call_args.kwargs["data"])
    assert request_data["method"] == "torrent-set-location"
    assert request_data["arguments"] == {
        "ids": [1, 2],
        "location": location,
        "move": True,
    }
