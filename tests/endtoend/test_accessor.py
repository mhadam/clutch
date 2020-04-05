import logging

# Enabling debugging at http.client level (requests->urllib3->http.client)
# you will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# the only thing missing will be the response.body which is not logged.
from http.client import HTTPConnection

from clutch.client import Client
from clutch.network.rpc.message import Response

HTTPConnection.debuglevel = 1  # type: ignore

logging.basicConfig()  # you need to initialize logging, otherwise you will not see anything from requests
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


def test_retrieve_all_fields():
    tag = 16
    client = Client(host="transmission")

    response: Response = client.torrent.accessor(all_fields=True, tag=tag)

    assert response.result == "success"
    assert response.tag == tag
    assert "little_women" in {x["name"] for x in response.dict(exclude_none=True)["arguments"]["torrents"]}
    assert "ion" in {x["name"] for x in response.dict(exclude_none=True)["arguments"]["torrents"]}


def test_retrieve_two_fields():
    tag = 16
    client = Client(host="transmission")

    response: Response = client.torrent.accessor(fields=['id', 'name'], tag=tag)

    assert response.result == "success"
    assert response.tag == tag
    assert 'id' in response.dict(exclude_none=True)["arguments"]["torrents"][0]
    assert 'name' in response.dict(exclude_none=True)["arguments"]["torrents"][0]
