from typing import Mapping


def combine_arguments(
    arguments: Mapping[str, object] | None = None, **kwargs
) -> Mapping[str, object]:
    if arguments is None:
        arguments = {}
    else:
        arguments = dict(arguments)
    arguments.update({k: v for k, v in kwargs.items() if v is not None})
    return arguments
