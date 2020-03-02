from typing import Mapping, Optional, Any

from clutch.network.rpc.message import Request


def construct_request(
    method: str,
    arguments: Optional[Mapping[str, Any]] = None,
    tag: Optional[int] = None,
) -> Request:
    request = Request(method=method)
    if arguments is not None:
        request["arguments"] = arguments
    if tag is not None:
        request["tag"] = tag
    return request
