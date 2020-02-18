from clutch.client import Client
from clutch.network.rpc.message import Response
from clutch.network.rpc.torrent.mutator import TorrentMutatorArguments

import logging

# Enabling debugging at http.client level (requests->urllib3->http.client)
# you will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# the only thing missing will be the response.body which is not logged.
from http.client import HTTPConnection

HTTPConnection.debuglevel = 1  # type: ignore

logging.basicConfig()  # you need to initialize logging, otherwise you will not see anything from requests
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


def test_server_returns_same_tag():
    tag = 15
    mutator_args: TorrentMutatorArguments = {}
    client = Client(host="transmission")

    response: Response = client.torrent_mutator(mutator_args, tag)

    assert response['tag'] == tag


def test_conversion_torrent_replace():
    pass
