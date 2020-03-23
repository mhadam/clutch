import re
from typing import TypeVar, Mapping, Callable, Union, Sequence

from clutch.network.rpc.message import Response

T = TypeVar("T", bound=Union[Mapping[str, object], Sequence])


def convert_response(
    received: Response[Mapping[str, object]],
    callback: Callable[[Union[Mapping[str, object], Sequence]], T] = None,
) -> Response[T]:
    if callback is None:
        callback = convert_response_arguments
    return Response(
        result=received.result, arguments=callback(received.arguments), tag=received.tag
    )


def convert_key(key: str) -> str:
    camelcase_split = re.split(r"(?<=[a-z])(?=[A-Z])", key)
    hyphen_split = key.split("-")
    if len(camelcase_split) > 1:
        return "_".join([word.lower() for word in camelcase_split])
    elif len(hyphen_split) > 1:
        return "_".join([word.lower() for word in hyphen_split])
    else:
        return key


def convert_response_arguments(
    arguments: Mapping[str, object], processors: Mapping[str, Callable] = None
) -> T:
    if processors is None:
        processors = {}

    result: T = {}
    for (key, value) in arguments.items():
        converted_key = convert_key(key)
        if converted_key in processors:
            result[converted_key] = processors[converted_key](value)
        else:
            result[converted_key] = value
    return result
