from typing import Optional

from clutch.method.method import MethodNamespace
from clutch.middle.session import convert_accessor, convert_mutator
from clutch.network.rpc.message import Response, Request
from clutch.network.rpc.session.shared import SessionArguments
from clutch.network.rpc.session.accessor import SessionAccessor
from clutch.network.rpc.session.mutator import SessionMutatorArguments, SessionMutator


class SessionMethods(MethodNamespace):
    def accessor(
        self, arguments: SessionArguments = None, tag: int = None,
    ) -> Optional[Response]:
        action = SessionAccessor(method="session-get")
        if arguments is not None:
            action["arguments"] = arguments
        if tag is not None:
            action["tag"] = tag

        request: Request = convert_accessor(action)
        return self._connection.send(request)

    def mutator(
        self, arguments: SessionMutatorArguments = None, tag: int = None
    ) -> Optional[Response]:
        action = SessionMutator(method="session-set", arguments=arguments)
        if tag is not None:
            action["tag"] = tag

        request: Request = convert_mutator(action)
        return self._connection.send(request)

    def stats(self, tag: int = None) -> Optional[Response]:
        request = Request(method="session-stats")
        if tag is not None:
            request["tag"] = tag
        return self._connection.send(request)

    def shutdown(self, tag: int = None) -> Optional[Response]:
        request = Request(method="session-close")
        if tag is not None:
            request["tag"] = tag
        return self._connection.send(request)
