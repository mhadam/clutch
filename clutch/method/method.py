from __future__ import annotations

from typing import TypeVar
from weakref import proxy

from clutch.network.connection import Connection

T = TypeVar("T", bound="MethodNamespace")


class MethodNamespace:

    def __get__(self: T, instance, owner) -> T:
        connection: Connection = instance.__dict__["_connection"]
        self._connection: Connection = proxy(connection)
        return self
