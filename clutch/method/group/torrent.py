from typing import Mapping

from clutch.method.convert.argument.torrent import (
    convert_mutator,
    convert_accessor,
    convert_add,
    convert_remove,
)
from clutch.method.convert.response.shared import convert_response
from clutch.method.convert.response.torrent import (
    convert_add_response,
    convert_accessor_response,
)
from clutch.method.group.method import MethodNamespace
from clutch.method.group.shared import construct_request
from clutch.method.typing.torrent.accessor import (
    TorrentAccessorResponse,
    field_keys,
)
from clutch.method.typing.torrent.action import (
    TorrentActionMethod,
    TorrentActionArguments,
)
from clutch.method.typing.torrent.add import TorrentAddArguments, TorrentAddResponse
from clutch.method.typing.torrent.move import TorrentMoveArguments
from clutch.method.typing.torrent.mutator import TorrentMutatorArguments
from clutch.method.typing.torrent.remove import TorrentRemoveArguments
from clutch.method.typing.torrent.rename import (
    TorrentRenameArguments,
    TorrentRenameResponse,
)
from clutch.network.rpc.message import Response


class TorrentMethods(MethodNamespace):
    def action(
        self,
        method: TorrentActionMethod,
        arguments: TorrentActionArguments = None,
        tag: int = None,
    ) -> Response[Mapping[str, object]]:
        """Start, stop, verify or reannounce a torrent."""
        request = construct_request(method.value, arguments, tag=tag)
        response = self._connection.send(request)
        return convert_response(response)

    def mutator(
        self, arguments: TorrentMutatorArguments = None, tag: int = None
    ) -> Response[Mapping[str, object]]:
        """Set a property of one or more torrents."""
        request = construct_request(
            method="torrent-set",
            arguments=arguments,
            arguments_callback=convert_mutator,
            tag=tag,
        )
        response = self._connection.send(request)
        return convert_response(response)

    def accessor(
        self,
        fields=None,
        *,
        all_fields=False,
        ids=None,
        response_format=None,
        tag: int = None
    ) -> Response[TorrentAccessorResponse]:
        """Retrieve information about one or more torrents."""
        if response_format is None:
            response_format = "objects"

        if all_fields:
            fields = field_keys
        elif fields is None:
            fields = []

        arguments = {
            "fields": fields,
            "format": response_format,
        }
        if ids is not None:
            if isinstance(ids, list):
                arguments["ids"] = ids
            else:
                pass
        request = construct_request(
            method="torrent-get",
            arguments=arguments,
            arguments_callback=convert_accessor,
            tag=tag,
        )
        response = self._connection.send(request)
        return convert_response(response, callback=convert_accessor_response)

    def add(
        self, arguments: TorrentAddArguments, tag: int = None
    ) -> Response[TorrentAddResponse]:
        """Add a new torrent."""
        request = construct_request(
            method="torrent-add",
            arguments=arguments,
            arguments_callback=convert_add,
            tag=tag,
        )
        response = self._connection.send(request)
        return convert_response(response, callback=convert_add_response)

    def move(
        self, arguments: TorrentMoveArguments, tag: int = None
    ) -> Response[Mapping[str, object]]:
        """Change the storage location of a torrent."""
        request = construct_request(
            method="torrent-set-location", arguments=arguments, tag=tag,
        )
        response = self._connection.send(request)
        return convert_response(response)

    def remove(
        self, arguments: TorrentRemoveArguments, tag: int = None
    ) -> Response[Mapping[str, object]]:
        """Remove one or more torrents."""
        request = construct_request(
            method="torrent-remove",
            arguments=arguments,
            arguments_callback=convert_remove,
            tag=tag,
        )
        response = self._connection.send(request)
        return convert_response(response)

    def rename(
        self, arguments: TorrentRenameArguments, tag: int = None
    ) -> Response[TorrentRenameResponse]:
        """Rename a file or directory in a torrent."""
        request = construct_request(
            method="torrent-rename-path", arguments=arguments, tag=tag,
        )
        response = self._connection.send(request)
        return convert_response(response)
