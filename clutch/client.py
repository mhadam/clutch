from typing import Optional

from clutch.middle import (
    convert_mutator,
    convert_action,
    convert_accessor,
    convert_add,
    convert_move,
    convert_remove,
    convert_rename,
)
from clutch.network.connection import Connection
from clutch.network.rpc.message import Response, Request
from clutch.network.rpc.torrent.accessor import (
    TorrentAccessorArguments,
    TorrentAccessor,
)
from clutch.network.rpc.torrent.action import (
    TorrentAction,
    TorrentActionMethod,
    TorrentActionArguments,
)
from clutch.network.rpc.torrent.add import TorrentAddArguments, TorrentAdd
from clutch.network.rpc.torrent.move import TorrentMoveArguments, TorrentMove
from clutch.network.rpc.torrent.mutator import TorrentMutator, TorrentMutatorArguments
from clutch.network.rpc.torrent.remove import TorrentRemoveArguments, TorrentRemove
from clutch.network.rpc.torrent.rename import TorrentRename, TorrentRenameArguments
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
        self.endpoint: str = make_endpoint(address, scheme, host, port, path, query)
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

        request: Request = convert_action(action)
        return self.connection.send(request)

    def torrent_mutator(
        self, arguments: TorrentMutatorArguments = None, tag: int = None
    ) -> Optional[Response]:
        mutator = TorrentMutator(method="torrent-set")
        if arguments is not None:
            mutator["arguments"] = arguments
        if tag is not None:
            mutator["tag"] = tag

        request: Request = convert_mutator(mutator)
        return self.connection.send(request)

    def torrent_accessor(
        self, arguments: TorrentAccessorArguments = None, tag: int = None
    ) -> Optional[Response]:
        accessor = TorrentAccessor(method="torrent-get")
        if arguments is not None:
            accessor["arguments"] = arguments
        if tag is not None:
            accessor["tag"] = tag

        request: Request = convert_accessor(accessor)
        return self.connection.send(request)

    def torrent_add(
        self, arguments: TorrentAddArguments, tag: int = None
    ) -> Optional[Response]:
        command = TorrentAdd(method="torrent-add", arguments=arguments)
        if tag is not None:
            command["tag"] = tag

        request: Request = convert_add(command)
        return self.connection.send(request)

    def torrent_move(
        self, arguments: TorrentMoveArguments, tag: int = None
    ) -> Optional[Response]:
        command = TorrentMove(method="torrent-move", arguments=arguments)
        if tag is not None:
            command["tag"] = tag

        request: Request = convert_move(command)
        return self.connection.send(request)

    def torrent_remove(
        self, arguments: TorrentRemoveArguments, tag: int = None
    ) -> Optional[Response]:
        command = TorrentRemove(method="torrent-remove", arguments=arguments)
        if tag is not None:
            command["tag"] = tag

        request: Request = convert_remove(command)
        return self.connection.send(request)

    def torrent_rename(
        self, arguments: TorrentRenameArguments, tag: int = None
    ) -> Optional[Response]:
        accessor = TorrentRename(method="torrent-rename", arguments=arguments)
        if tag is not None:
            accessor["tag"] = tag

        request: Request = convert_rename(accessor)
        return self.connection.send(request)
