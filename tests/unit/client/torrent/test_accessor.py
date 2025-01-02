from json import loads


def test_torrent_accessor_fields(client):
    try:
        client.torrent.accessor(fields=["peer_limit", "tracker_stats"])
    except:
        pass

    request_data = loads(client._connection.session.post.call_args.kwargs["data"])
    assert request_data["method"] == "torrent-get"
    assert set(request_data["arguments"]["fields"]) == {"peer-limit", "trackerStats"}
    assert request_data["arguments"]["format"] == "objects"
