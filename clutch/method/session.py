from clutch.method.method import MethodNamespace
from clutch.network.rpc.message import Response, Request
from clutch.schema.request.session.accessor import (
    SessionAccessorFields,
    SessionAccessorArgumentsRequest,
)
from clutch.schema.request.session.mutator import SessionMutatorArgumentsRequest


from clutch.schema.user.method.session.mutator import SessionMutatorArguments
from clutch.schema.user.response.session.accessor import SessionAccessor
from clutch.schema.user.response.session.stats import SessionStats


class SessionMethods(MethodNamespace):
    def accessor(
        self, tag: int = None,
    ) -> Response[SessionAccessor]:
        """Retrieve information about one or more torrents."""
        return self._connection.send(
            Request[SessionAccessorArgumentsRequest](
                method="session-get", arguments={"fields": None}, tag=tag  # fields doesn't work as spec'd, 3.0?
            ),
            SessionAccessor,
        )

    def mutator(self, arguments: SessionMutatorArguments, tag: int = None) -> Response:
        """Set a property of one or more torrents."""
        return self._connection.send(
            Request[SessionMutatorArgumentsRequest](
                method="session-set", arguments=arguments, tag=tag
            )
        )

    def stats(self, tag: int = None) -> Response[SessionStats]:
        """Retrieve all session statistics."""
        return self._connection.send(
            Request(method="session-stats", tag=tag), SessionStats
        )

    def shutdown(self, tag: int = None) -> Response:
        """Shutdown the torrent client."""
        return self._connection.send(Request(method="session-close", tag=tag))
