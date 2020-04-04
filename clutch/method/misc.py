from clutch.method.method import MethodNamespace
from clutch.network.rpc.message import Response, Request
from clutch.schema.user.response.misc import (
    BlocklistResponse,
    PortTestResponse,
    FreeSpaceResponse,
)


class MiscellaneousMethods(MethodNamespace):
    def blocklist_update(self, tag: int = None) -> Response[BlocklistResponse]:
        """Trigger an update of the client blocklist."""
        return self._connection.send(
            Request(method="blocklist-update", tag=tag), BlocklistResponse
        )

    def port_test(self, tag: int = None) -> Response[PortTestResponse]:
        """Test the client to see if the port settings are open for connections."""
        return self._connection.send(
            Request(method="port-test", tag=tag), PortTestResponse
        )

    def free_space(self, path: str, tag: int = None) -> Response[FreeSpaceResponse]:
        """Query for available free-space in the specified path."""
        return self._connection.send(
            Request(method="free-space", arguments={"path": path}, tag=tag),
            FreeSpaceResponse,
        )
