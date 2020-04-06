from json import loads

from clutch.method.queue import QueueMovement


def test_queue_move(client):
    try:
        client.queue.move(movement=QueueMovement.TOP, ids=[1, 2])
    except Exception as e:
        pass

    request_data = loads(client._connection.session.post.call_args.kwargs["data"])
    assert request_data["method"] == QueueMovement.TOP.value
    assert request_data["arguments"] == {"ids": [1, 2]}
