from json import loads
from unittest.mock import create_autospec

from clutch.client import Client
from clutch.network.connection import Connection
from clutch.network.session import TransmissionSession


def test_torrent_accessor():
    session = create_autospec(TransmissionSession)
    connection = Connection("127.0.0.1", session)
    client = Client()
    client._connection = connection

    try:
        client.torrent.accessor()
    except Exception:
        pass

    request_data = loads(client._connection.session.post.call_args.kwargs['data'])
    assert request_data['method'] == 'torrent-get'
    assert request_data['arguments']['fields'] == []
    assert request_data['arguments']['format'] == "objects"
