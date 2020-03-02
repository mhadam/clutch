import logging

# Enabling debugging at http.client level (requests->urllib3->http.client)
# you will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# the only thing missing will be the response.body which is not logged.
from http.client import HTTPConnection

from clutch.client import Client
from clutch.network.rpc.message import Response
from clutch.network.rpc.torrent.accessor import TorrentAccessorArguments

HTTPConnection.debuglevel = 1  # type: ignore

logging.basicConfig()  # you need to initialize logging, otherwise you will not see anything from requests
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


def test_retrieving_all_names():
    tag = 16
    accessor_args: TorrentAccessorArguments = {"fields": {"name"}}
    client = Client(host="transmission")

    response: Response = client.torrent.accessor(accessor_args, tag)

    assert response["result"] == "success"
    assert response["tag"] == tag
    assert "little_women" in {x["name"] for x in response["arguments"]["torrents"]}
    assert "ion" in {x["name"] for x in response["arguments"]["torrents"]}
