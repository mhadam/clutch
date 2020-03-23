from dataclasses import dataclass
from typing import TypedDict, Mapping, Any, TypeVar, Generic

T = TypeVar("T", bound=Mapping[str, object])


class OptionalMessageFields(TypedDict, total=False):
    """RPC message optional fields"""

    arguments: Mapping[str, Any]
    tag: int


class Request(OptionalMessageFields):
    """RPC request container"""

    method: str


@dataclass
class Response(Generic[T]):
    """RPC response container"""

    result: str
    arguments: T = None
    tag: int = None
