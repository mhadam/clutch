from clutch.method.method import MethodNamespace
from clutch.network.rpc.message import Request, Response
from clutch.schema.request.misc.port_test import PortTestArgumentsRequest
from clutch.schema.user.method.misc import IpProtocol
from clutch.schema.user.response.misc import (
    BandwidthGroupResponse,
    BlocklistResponse,
    FreeSpaceResponse,
    PortTestResponse,
)


class MiscellaneousMethods(MethodNamespace):
    def blocklist_update(self, tag: int | None = None) -> Response[BlocklistResponse]:
        """Trigger an update of the client blocklist."""
        return self._connection.send(
            Request(method="blocklist-update", tag=tag), BlocklistResponse
        )

    def port_test(
        self, ip_protocol: IpProtocol | None = None, tag: int | None = None
    ) -> Response[PortTestResponse]:
        """Test the client to see if the port settings are open for connections."""
        return self._connection.send(
            Request[PortTestArgumentsRequest](
                method="port-test", arguments={"ip_protocol": ip_protocol}, tag=tag
            ),
            PortTestResponse,
        )

    def free_space(
        self, path: str, tag: int | None = None
    ) -> Response[FreeSpaceResponse]:
        """Query for available free-space in the specified path."""
        return self._connection.send(
            Request(method="free-space", arguments={"path": path}, tag=tag),
            FreeSpaceResponse,
        )

    def bandwidth_groups(
        self, group: str | list[str] | None = None, tag: int | None = None
    ) -> Response[BandwidthGroupResponse]:
        """Query for bandwidth groups."""
        return self._connection.send(
            Request(method="group-get", arguments={"group": group}, tag=tag),
            BandwidthGroupResponse,
        )
