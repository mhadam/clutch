from typing import Optional

from clutch.method.convert.argument.session import convert_accessor, convert_mutator
from clutch.method.method import MethodNamespace
from clutch.method.shared import construct_request
from clutch.method.typing.session.accessor import SessionAccessorArguments
from clutch.method.typing.session.mutator import SessionMutatorArguments
from clutch.network.rpc.message import Response


class SessionMethods(MethodNamespace):
    def accessor(
        self, arguments: SessionAccessorArguments = None, tag: int = None,
    ) -> Optional[Response]:
        request = construct_request(
            method="session-get",
            arguments=arguments,
            arguments_callback=convert_accessor,
            tag=tag,
        )
        return self._connection.send(request)

    def mutator(
        self, arguments: SessionMutatorArguments, tag: int = None
    ) -> Optional[Response]:
        request = construct_request(
            method="session-set",
            arguments=arguments,
            arguments_callback=convert_mutator,
            tag=tag,
        )
        return self._connection.send(request)

    def stats(self, tag: int = None) -> Optional[Response]:
        request = construct_request(method="session-stats", tag=tag)
        return self._connection.send(request)

    def shutdown(self, tag: int = None) -> Optional[Response]:
        request = construct_request(method="session-close", tag=tag)
        return self._connection.send(request)
