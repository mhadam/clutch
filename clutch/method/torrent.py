from typing import Literal, Sequence, Set, Union

from clutch.method.method import MethodNamespace
from clutch.method.shared import combine_arguments
from clutch.network.rpc.message import Request, Response
from clutch.schema.request.torrent.accessor import TorrentAccessorArgumentsRequest
from clutch.schema.request.torrent.add import TorrentAddArgumentsRequest
from clutch.schema.request.torrent.mutator import TorrentMutatorArgumentsRequest
from clutch.schema.user.method.shared import IdsArg
from clutch.schema.user.method.torrent.accessor import TorrentAccessorField, field_keys
from clutch.schema.user.method.torrent.action import TorrentActionMethod
from clutch.schema.user.method.torrent.add import TorrentAddArguments
from clutch.schema.user.method.torrent.mutator import TorrentMutatorArguments
from clutch.schema.user.response.torrent.accessor import TorrentAccessorResponse
from clutch.schema.user.response.torrent.add import TorrentAdd
from clutch.schema.user.response.torrent.rename import TorrentRename


class TorrentMethods(MethodNamespace):
    def accessor(
        self,
        fields: Set[TorrentAccessorField] | None = None,
        *,
        all_fields: bool = False,
        ids: IdsArg | None = None,
        response_format: Literal["objects", "table"] | None = None,
        tag: int | None = None,
    ) -> Response[TorrentAccessorResponse]:
        """Retrieve information about one or more torrents."""
        if response_format is None:
            response_format = "objects"

        if all_fields:
            fields = field_keys
        elif fields is None:
            fields = set()

        combined_arguments = combine_arguments(
            accessor_fields=fields, format=response_format, ids=ids
        )
        return self._connection.send(
            Request[TorrentAccessorArgumentsRequest](
                method="torrent-get", arguments=combined_arguments, tag=tag
            ),
            TorrentAccessorResponse,
        )

    def action(
        self,
        method: TorrentActionMethod,
        ids: IdsArg | None = None,
        tag: int | None = None,
    ) -> Response:
        """Start, stop, verify or reannounce a torrent."""
        return self._connection.send(
            Request(method=method.value, arguments={"ids": ids}, tag=tag)
        )

    def add(
        self, arguments: TorrentAddArguments, tag: int | None = None
    ) -> Response[TorrentAdd]:
        """Add a new torrent."""
        return self._connection.send(
            Request[TorrentAddArgumentsRequest](
                method="torrent-add", arguments=arguments, tag=tag
            ),
            TorrentAdd,
        )

    def mutator(
        self,
        ids: IdsArg | None = None,
        arguments: TorrentMutatorArguments | None = None,
        tag: int | None = None,
    ) -> Response:
        """Set a property of one or more torrents."""
        try:
            arguments["tracker_list"] = "\n\n".join(
                "\n".join(x) for x in arguments["tracker_list"]
            )
        except (KeyError, TypeError):
            pass
        return self._connection.send(
            Request[TorrentMutatorArgumentsRequest](
                method="torrent-set",
                arguments=combine_arguments(arguments, ids=ids),
                tag=tag,
            )
        )

    def move(
        self, ids: IdsArg, location: str, move: bool = False, tag: int | None = None
    ) -> Response:
        """Change the storage location of a torrent."""
        return self._connection.send(
            Request(
                method="torrent-set-location",
                arguments=combine_arguments(ids=ids, location=location, move=move),
                tag=tag,
            )
        )

    def remove(
        self, ids: IdsArg, delete_local_data: bool = False, tag: int | None = None
    ) -> Response:
        """Remove one or more torrents."""
        return self._connection.send(
            Request(
                method="torrent-remove",
                arguments={"ids": ids, "delete-local-data": delete_local_data},
                tag=tag,
            )
        )

    def rename(
        self,
        ids: Sequence[Union[str, int]],
        path: str,
        name: str,
        tag: int | None = None,
    ) -> Response[TorrentRename]:
        """Rename a file or directory in a torrent."""
        return self._connection.send(
            Request(
                method="torrent-rename-path",
                arguments=combine_arguments(ids=ids, path=path, name=name),
                tag=tag,
            ),
            TorrentRename,
        )
