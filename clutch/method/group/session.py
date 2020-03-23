from typing import Optional, Mapping

from clutch.method.convert.argument.session import convert_accessor, convert_mutator
from clutch.method.convert.response.session import (
    convert_stats,
    convert_accessor_response,
)
from clutch.method.convert.response.shared import convert_response
from clutch.method.group.method import MethodNamespace
from clutch.method.group.shared import construct_request
from clutch.method.typing.session.accessor import (
    SessionAccessorArguments,
    SessionAccessorResponse,
)
from clutch.method.typing.session.mutator import SessionMutatorArguments
from clutch.method.typing.session.stats import SessionStatsResponse
from clutch.network.rpc.message import Response


class SessionMethods(MethodNamespace):
    def accessor(
        self, arguments: SessionAccessorArguments = None, tag: int = None,
    ) -> Response[SessionAccessorResponse]:
        """Retrieve information about one or more torrents."""
        request = construct_request(
            method="session-get",
            arguments=arguments,
            arguments_callback=convert_accessor,
            tag=tag,
        )
        response = self._connection.send(request)
        return convert_response(response, callback=convert_accessor_response)

    def mutator(
        self, arguments: SessionMutatorArguments, tag: int = None
    ) -> Response[Mapping[str, object]]:
        """Set a property of one or more torrents."""

        request = construct_request(
            method="session-set",
            arguments=arguments,
            arguments_callback=convert_mutator,
            tag=tag,
        )
        return self._connection.send(request)

    def stats(self, tag: int = None) -> Response[SessionStatsResponse]:
        """Retrieve all session statistics."""
        request = construct_request(method="session-stats", tag=tag)
        response = self._connection.send(request)
        return convert_response(response, convert_stats)

    def shutdown(self, tag: int = None) -> Response[Mapping[str, object]]:
        """Shutdown the torrent client."""
        request = construct_request(method="session-close", tag=tag)
        return self._connection.send(request)
