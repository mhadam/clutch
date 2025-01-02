from json import loads


def test_torrent_mutator(client):
    try:
        client.torrent.mutator()
    except Exception:
        pass

    request_data = loads(client._connection.session.post.call_args.kwargs["data"])
    assert request_data["method"] == "torrent-set"
    assert request_data["arguments"] == {}


def test_torrent_mutator_arguments(client):
    try:
        client.torrent.mutator(
            ids=["hi", 2],
            arguments={"priority_high": [], "download_limited": True, "ids": [3, 4]},
        )
    except Exception as e:
        pass

    request_data = loads(client._connection.session.post.call_args.kwargs["data"])
    assert request_data["method"] == "torrent-set"
    # turn ids into a set since pydantic seems to serialize as a set
    # and original ids order differs from assertion
    assert len(set(request_data["arguments"]["ids"])) == len(
        request_data["arguments"]["ids"]
    )
    request_data["arguments"]["ids"] = set(request_data["arguments"]["ids"])
    assert request_data["arguments"] == {
        "ids": {"hi", 2},
        "downloadLimited": True,
        "priority-high": [],
    }
