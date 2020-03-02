from typing import Optional

from requests import Response

from clutch.method.method import MethodNamespace
from clutch.network.rpc.message import Request


class MiscellaneousMethods(MethodNamespace):

    def blocklist_update(self, tag: int = None) -> Optional[Response]:
        request = Request(method="blocklist-update")
        if tag is not None:
            request["tag"] = tag
        return self._connection.send(request)

    def port_test(self, tag: int = None) -> Optional[Response]:
        request = Request(method="port-test")
        if tag is not None:
            request["tag"] = tag
        return self._connection.send(request)

    def free_space(self, path: str, tag: int = None):
        request = Request(method="free-space")
        request["arguments"] = {"path": path}
        if tag is not None:
            request["tag"] = tag
        return self._connection.send(request)
