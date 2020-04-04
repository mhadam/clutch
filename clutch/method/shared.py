from typing import Mapping


def combine_arguments(
    arguments: Mapping[str, object] = None, **kwargs
) -> Mapping[str, object]:
    if arguments is None:
        arguments = {}
    else:
        arguments = dict(arguments)
    arguments.update(kwargs)
    return arguments
