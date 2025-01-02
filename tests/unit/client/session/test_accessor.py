from json import loads

from dirty_equals import IsList


def test_session_accessor(client):
    tag = 5
    try:
        client.session.accessor(fields={"rpc_version", "seed_ratio_limit"}, tag=tag)
    except Exception as e:
        print(e)

    request_data = loads(client._connection.session.post.call_args.kwargs["data"])
    assert request_data["method"] == "session-get"
    assert request_data["arguments"] == {
        "fields": IsList("rpc-version", "seedRatioLimit", check_order=False)
    }
    assert request_data["tag"] == tag
