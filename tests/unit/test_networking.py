from typing import Optional
from unittest.mock import create_autospec

from clutch.network.connection import Connection
from clutch.network.rpc.message import Request, Response
from clutch.network.session import TransmissionSession
from clutch.schema.user.response.torrent.accessor import TorrentAccessorResponse


def test_connection_marshals_requests_and_responses():
    session = create_autospec(TransmissionSession)
    session.post.return_value.text = (
        '{"result":"success","arguments":{"test":"response"},"tag":5}'
    )
    connection = Connection("127.0.0.1", session)
    request = Request(method="torrent-get", arguments={"test": "request"}, tag=5)

    response: Optional[Response] = connection.send(request)

    assert response is not None
    assert response.arguments["test"] == "response"
    assert response.tag == 5
    assert response.result == "success"


def test_connection_marshals_types():
    session = create_autospec(TransmissionSession)
    session.post.return_value.text = (
        '{"result":"success","arguments":{"torrents":[{"id":1},{"id":2}]},"tag":5}'
    )
    connection = Connection("127.0.0.1", session)
    request = Request(method="torrent-get", arguments={"fields": ["id"]}, tag=5)

    response = connection.send(request, TorrentAccessorResponse)

    assert response is not None
    assert isinstance(response.arguments, TorrentAccessorResponse)
    assert response.arguments.dict(exclude_none=True)["torrents"] == [
        {"id": 1},
        {"id": 2},
    ]
    assert response.tag == 5
    assert response.result == "success"
