from typing import Optional

from clutch.method.convert.argument.torrent import (
    convert_mutator,
    convert_accessor,
    convert_add,
    convert_remove,
)
from clutch.method.method import MethodNamespace
from clutch.method.shared import construct_request
from clutch.method.typing.torrent.accessor import TorrentAccessorArguments
from clutch.method.typing.torrent.action import (
    TorrentActionMethod,
    TorrentActionArguments,
)
from clutch.method.typing.torrent.add import TorrentAddArguments
from clutch.method.typing.torrent.move import TorrentMoveArguments
from clutch.method.typing.torrent.mutator import TorrentMutatorArguments
from clutch.method.typing.torrent.remove import TorrentRemoveArguments
from clutch.method.typing.torrent.rename import TorrentRenameArguments
from clutch.network.rpc.message import Response


class TorrentMethods(MethodNamespace):
    def action(
        self,
        method: TorrentActionMethod,
        arguments: TorrentActionArguments = None,
        tag: int = None,
    ) -> Optional[Response]:
        request = construct_request(method.value, arguments, tag=tag)
        return self._connection.send(request)

    def mutator(
        self, arguments: TorrentMutatorArguments = None, tag: int = None
    ) -> Optional[Response]:
        request = construct_request(
            method="torrent-set",
            arguments=arguments,
            arguments_callback=convert_mutator,
            tag=tag,
        )
        return self._connection.send(request)

    def accessor(
        self, arguments: TorrentAccessorArguments = None, tag: int = None
    ) -> Optional[Response]:
        request = construct_request(
            method="torrent-get",
            arguments=arguments,
            arguments_callback=convert_accessor,
            tag=tag,
        )
        return self._connection.send(request)

    def add(
        self, arguments: TorrentAddArguments, tag: int = None
    ) -> Optional[Response]:
        request = construct_request(
            method="torrent-add",
            arguments=arguments,
            arguments_callback=convert_add,
            tag=tag,
        )
        return self._connection.send(request)

    def move(
        self, arguments: TorrentMoveArguments, tag: int = None
    ) -> Optional[Response]:
        request = construct_request(
            method="torrent-set-location", arguments=arguments, tag=tag,
        )
        return self._connection.send(request)

    def remove(
        self, arguments: TorrentRemoveArguments, tag: int = None
    ) -> Optional[Response]:
        request = construct_request(
            method="torrent-remove",
            arguments=arguments,
            arguments_callback=convert_remove,
            tag=tag,
        )
        return self._connection.send(request)

    def rename(
        self, arguments: TorrentRenameArguments, tag: int = None
    ) -> Optional[Response]:
        request = construct_request(
            method="torrent-rename-path", arguments=arguments, tag=tag,
        )
        return self._connection.send(request)
