from json import loads


def test_session_accessor(client):
    tag = 5
    try:
        client.session.accessor(tag=tag)
    except Exception:
        pass

    request_data = loads(client._connection.session.post.call_args.kwargs["data"])
    assert request_data["method"] == "session-get"
    assert request_data["arguments"] == {}
    assert request_data["tag"] == tag
