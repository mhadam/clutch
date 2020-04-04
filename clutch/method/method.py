from typing import TypeVar
from weakref import proxy

from clutch.network.connection import Connection

T = TypeVar("T", bound="MethodNamespace")


class MethodNamespace:
    _connection: Connection = ...  # type: ignore

    def __init__(self, client=None):
        if client is not None:
            self._connection = proxy(client.__dict__["_connection"])

    def __get__(self: T, instance, owner) -> T:
        return self.__class__(instance)
