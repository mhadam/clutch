from typing import TypeVar, Generic, Optional

from pydantic import validator
from pydantic.generics import GenericModel

from clutch.network.rpc.convert import normalize_arguments

T = TypeVar("T")


class Request(GenericModel, Generic[T]):
    """RPC request container"""

    method: str
    arguments: Optional[T] = None
    tag: Optional[int] = None


class Response(GenericModel, Generic[T]):
    """RPC response container"""

    result: str
    arguments: Optional[T] = None
    tag: Optional[int] = None

    @validator("arguments", pre=True)
    def fields_underscored(cls, v):
        if v is not None:
            return normalize_arguments(v)
        else:
            return v
