from json import loads


def test_session_mutator_arguments(client):
    try:
        client.session.mutator(
            arguments={"seed_ratio_limited": True, "seed_queue_size": 10}
        )
    except Exception as e:
        pass

    request_data = loads(client._connection.session.post.call_args.kwargs["data"])
    assert request_data["method"] == "session-set"
    assert request_data["arguments"] == {
        "seed-queue-size": 10,
        "seedRatioLimited": True,
    }
