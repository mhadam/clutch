import re
from typing import Mapping, MutableMapping, Union, Sequence


def to_underscore(key: str) -> str:
    camelcase_split = re.split(r"(?<=[a-z])(?=[A-Z])", key)
    hyphen_split = key.split("-")
    if len(camelcase_split) > 1:
        return "_".join([word.lower() for word in camelcase_split])
    elif len(hyphen_split) > 1:
        return "_".join([word.lower() for word in hyphen_split])
    else:
        return key


def to_camel(key: str) -> str:
    words = key.split("_")
    return "".join(words[:1] + [word.capitalize() for word in words[1:]])


def to_hyphen(key: str) -> str:
    return "-".join(key.split("_"))


def normalize_arguments(arguments: Mapping[str, object] = None) -> Mapping[str, object]:
    if arguments is None:
        return {}

    result: MutableMapping[str, object] = {}
    iterations = [(result, item) for item in arguments.items()]
    for iteration in iterations:
        parent: Union[MutableMapping[str, object], Sequence] = iteration[0]
        if isinstance(parent, dict):
            (key, value) = iteration[1]
            converted_key = to_underscore(key)
            if isinstance(value, dict):
                parent[converted_key] = {}
                iterations.extend(
                    [(parent[converted_key], item) for item in value.items()]
                )
            elif isinstance(value, list):
                parent[converted_key] = []
                iterations.extend([(parent[converted_key], item) for item in value])
            else:
                parent[converted_key] = value
        elif isinstance(parent, list):
            value = iteration[1]
            if isinstance(value, dict):
                new_element = {}
                parent.append(new_element)
                iterations.extend([(new_element, item) for item in value.items()])
            elif isinstance(value, list):
                new_element = []
                parent.append(new_element)
                iterations.extend([(new_element, item) for item in value])
            else:
                parent.append(value)
    return result
