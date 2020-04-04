from typing import Mapping, TypeVar

T = TypeVar("T", bound=Mapping[str, object], contravariant=True)


def combine_arguments(
    arguments: Mapping[str, object] = None, /, **kwargs
) -> Mapping[str, object]:
    if arguments is None:
        arguments = {}
    else:
        arguments = dict(arguments)
    arguments.update(kwargs)
    return arguments
