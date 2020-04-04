from typing import Optional
from unittest.mock import create_autospec

from clutch.network.connection import Connection
from clutch.network.rpc.message import Request, Response
from clutch.network.session import TransmissionSession
from clutch.schema.user.method.torrent.action import TorrentActionMethod


def test_connection_marshals_requests_and_responses():
    session = create_autospec(TransmissionSession)
    session.post.return_value.text = (
        '{"result":"success","arguments":{"test":"test"},"tag":1}'
    )
    connection = Connection("127.0.0.1", session)
    request = Request(method=TorrentActionMethod.REANNOUNCE.value)
    request["arguments"] = {"test": "test"}
    request["tag"] = 1
    response: Optional[Response] = connection.send(request)

    assert response is not None
    assert response["result"] == "success"
    assert response["arguments"] == {"test": "test"}
    assert response["tag"] == 1
