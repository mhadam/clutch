from typing import Optional

from clutch.method.method import MethodNamespace
from clutch.method.typing.torrent.accessor import TorrentAccessorArguments, TorrentAccessor
from clutch.method.typing.torrent.action import TorrentActionMethod, TorrentActionArguments, TorrentAction
from clutch.method.typing.torrent.add import TorrentAddArguments, TorrentAdd
from clutch.method.typing.torrent.move import TorrentMoveArguments, TorrentMove
from clutch.method.typing.torrent.mutator import TorrentMutatorArguments, TorrentMutator
from clutch.method.typing.torrent.remove import TorrentRemoveArguments, TorrentRemove
from clutch.method.typing.torrent.rename import TorrentRenameArguments, TorrentRename
from clutch.middle.torrent import (
    convert_mutator,
    convert_accessor,
    convert_action,
    convert_add,
    convert_move,
    convert_remove,
    convert_rename,
)
from clutch.network.rpc.message import Response, Request


class TorrentMethods(MethodNamespace):
    def action(
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
        return self._connection.send(request)

    def mutator(
        self, arguments: TorrentMutatorArguments = None, tag: int = None
    ) -> Optional[Response]:
        mutator = TorrentMutator(method="torrent-set")
        if arguments is not None:
            mutator["arguments"] = arguments
        if tag is not None:
            mutator["tag"] = tag

        request: Request = convert_mutator(mutator)
        return self._connection.send(request)

    def accessor(
        self, arguments: TorrentAccessorArguments = None, tag: int = None
    ) -> Optional[Response]:
        accessor = TorrentAccessor(method="torrent-get")
        if arguments is not None:
            accessor["arguments"] = arguments
        if tag is not None:
            accessor["tag"] = tag

        request: Request = convert_accessor(accessor)
        return self._connection.send(request)

    def add(
        self, arguments: TorrentAddArguments, tag: int = None
    ) -> Optional[Response]:
        command = TorrentAdd(method="torrent-add", arguments=arguments)
        if tag is not None:
            command["tag"] = tag

        request: Request = convert_add(command)
        return self._connection.send(request)

    def move(
        self, arguments: TorrentMoveArguments, tag: int = None
    ) -> Optional[Response]:
        command = TorrentMove(method="torrent-move", arguments=arguments)
        if tag is not None:
            command["tag"] = tag

        request: Request = convert_move(command)
        return self._connection.send(request)

    def remove(
        self, arguments: TorrentRemoveArguments, tag: int = None
    ) -> Optional[Response]:
        command = TorrentRemove(method="torrent-remove", arguments=arguments)
        if tag is not None:
            command["tag"] = tag

        request: Request = convert_remove(command)
        return self._connection.send(request)

    def rename(
        self, arguments: TorrentRenameArguments, tag: int = None
    ) -> Optional[Response]:
        accessor = TorrentRename(method="torrent-rename", arguments=arguments)
        if tag is not None:
            accessor["tag"] = tag

        request: Request = convert_rename(accessor)
        return self._connection.send(request)
