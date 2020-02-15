from typing import AnyStr, Optional

from clutch.middle import convert_mutator
from clutch.network.connection import Connection
from clutch.network.rpc.message import Response
from clutch.network.rpc.torrent.action import (
    TorrentAction,
    TorrentActionMethod,
    TorrentActionArguments,
)
from clutch.network.rpc.torrent.mutator import TorrentMutator, TorrentMutatorArguments
from clutch.network.session import TransmissionSession
from clutch.network.utility import make_endpoint


class Client:
    def __init__(
        self,
        address="http://localhost:9091/transmission/rpc",
        scheme=None,
        host=None,
        port=None,
        path=None,
        query=None,
        username=None,
        password=None,
        timeout=None,
    ):
        self._rpc_version = None
        self.timeout = timeout
        self.endpoint: AnyStr = make_endpoint(address, scheme, host, port, path, query)
        self.session: TransmissionSession = TransmissionSession(username, password)
        self.connection: Connection = Connection(self.endpoint, self.session)

    def torrent_action(
        self,
        method: TorrentActionMethod,
        arguments: TorrentActionArguments = None,
        tag: int = None,
    ) -> Optional[Response]:
        action = TorrentAction(method=method)
        if arguments is not None:
            action["arguments"] = arguments
        if tag is not None:
            action["tag"] = tag
        return self.connection.send()

    def torrent_mutator(
        self, arguments: TorrentMutatorArguments = None, tag: int = None
    ) -> Optional[Response]:
        mutator = TorrentMutator(method="torrent-set")
        if arguments is not None:
            mutator["arguments"] = arguments
        if tag is not None:
            mutator["tag"] = tag

        converted_mutator = convert_mutator(mutator)
        if converted_mutator is not None:
            if response := self.connection.send(converted_mutator):
                return response
        return None
