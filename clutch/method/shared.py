from typing import Mapping, Optional, Protocol, TypeVar, FrozenSet

from clutch.method.convert.argument.torrent import convert_arguments
from clutch.network.rpc.message import Request

T = TypeVar("T", bound=Mapping[str, object], contravariant=True)


class ArgumentsCallback(Protocol[T]):
    def __call__(self, arguments: T) -> Mapping[str, object]:
        pass


def construct_request(
    method: str,
    arguments: T = None,
    arguments_callback: ArgumentsCallback[T] = None,
    tag: Optional[int] = None,
    *,
    hyphenate: FrozenSet[str] = None,
    camelcase: FrozenSet[str] = None,
    default_hyphenate: bool = None,
    default_camelcase: bool = None,
) -> Request:
    request = Request(method=method)
    if arguments is not None:
        if arguments_callback is not None:
            request["arguments"] = arguments_callback(arguments)
        else:
            request["arguments"] = convert_arguments(
                arguments,
                hyphenate=hyphenate,
                camelcase=camelcase,
                default_camelcase=default_camelcase,
                default_hyphenate=default_hyphenate,
            )
    if tag is not None:
        request["tag"] = tag
    return request
