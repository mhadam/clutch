from typing import TypedDict, Mapping, Any


class OptionalMessageFields(TypedDict, total=False):
    """RPC message optional fields"""

    arguments: Mapping[str, Any]
    tag: int


class Request(OptionalMessageFields):
    """RPC request container"""

    method: str


class Response(OptionalMessageFields):
    """RPC response container"""

    result: str
