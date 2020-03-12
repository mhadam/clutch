from typing import Optional

from clutch.method.method import MethodNamespace
from clutch.method.shared import construct_request
from clutch.network.rpc.message import Response


class MiscellaneousMethods(MethodNamespace):
    def blocklist_update(self, tag: int = None) -> Optional[Response]:
        request = construct_request("blocklist-update", tag=tag)
        return self._connection.send(request)

    def port_test(self, tag: int = None) -> Optional[Response]:
        request = construct_request("port-test", tag=tag)
        return self._connection.send(request)

    def free_space(self, path: str, tag: int = None) -> Optional[Response]:
        request = construct_request("free-space", {"path": path}, tag=tag)
        return self._connection.send(request)
