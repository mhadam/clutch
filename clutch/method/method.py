from __future__ import annotations

from typing import Optional, TypeVar
from weakref import CallableProxyType, proxy

from clutch.network.connection import Connection

T = TypeVar("T", bound="MethodNamespace")


class MethodNamespace:
    def __init__(self):
        self._connection: CallableProxyType[Connection] = None

    def __get__(self: T, instance, owner) -> T:
        self._connection = proxy(instance.__dict__["_connection"])
        return self
