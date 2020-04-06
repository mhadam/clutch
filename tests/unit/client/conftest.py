from unittest.mock import create_autospec

import pytest

from clutch.client import Client
from clutch.network.connection import Connection
from clutch.network.session import TransmissionSession


@pytest.fixture(scope="function")
def client():
    session = create_autospec(TransmissionSession)
    connection = Connection("127.0.0.1", session)
    client = Client()
    client._connection = connection
    return client
