from clutch.method.convert.response.misc import (
    FreeSpaceResponse,
    BlocklistResponse,
    PortTestResponse,
)
from clutch.method.convert.response.shared import convert_response
from clutch.method.group.method import MethodNamespace
from clutch.method.group.shared import construct_request
from clutch.network.rpc.message import Response


class MiscellaneousMethods(MethodNamespace):
    def blocklist_update(self, tag: int = None) -> Response[BlocklistResponse]:
        """Trigger an update of the client blocklist."""
        request = construct_request("blocklist-update", tag=tag)
        response = self._connection.send(request)
        return convert_response(response)

    def port_test(self, tag: int = None) -> Response[PortTestResponse]:
        """Test the client to see if the port settings are open for connections."""
        request = construct_request("port-test", tag=tag)
        response = self._connection.send(request)
        return convert_response(response)

    def free_space(self, path: str, tag: int = None) -> Response[FreeSpaceResponse]:
        """Query for available free-space in the specified path."""
        request = construct_request("free-space", {"path": path}, tag=tag)
        response = self._connection.send(request)
        return convert_response(response)
