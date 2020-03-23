from functools import partial
from typing import FrozenSet, Mapping, Callable, MutableMapping, Sequence


def _camelcase(words: Sequence[str]) -> str:
    try:
        return "".join(list(words[0]) + [word.capitalize() for word in words[1:]])
    except IndexError:
        pass


def normalize_key(
    key: str,
    hyphenate: FrozenSet[str] = None,
    camelcase: FrozenSet[str] = None,
    default_hyphenate: bool = None,
    default_camelcase: bool = None,
) -> str:
    """Takes a key with underscore format and converts to hyphenated or preferably camelcase."""
    if default_hyphenate and default_camelcase:
        raise ValueError(
            "Select either default_hyphenated or default_camelcase, not both"
        )
    words = key.split("_")
    camelcase_result = _camelcase(words)
    hyphenated_result = "-".join(words)

    if camelcase is None:
        camelcase = frozenset()
    if key in camelcase:
        return camelcase_result

    if hyphenate is None:
        hyphenate = frozenset()
    if key in hyphenate:
        return hyphenated_result

    if default_camelcase:
        return _camelcase(words)
    elif default_hyphenate:
        return hyphenated_result
    else:
        return camelcase_result


def convert_arguments(
    arguments: Mapping[str, object],
    processors: Mapping[str, Callable] = None,
    *,
    hyphenate: FrozenSet[str] = None,
    camelcase: FrozenSet[str] = None,
    default_hyphenate: bool = None,
    default_camelcase: bool = None,
) -> Mapping[str, object]:
    result: MutableMapping[str, object] = {}
    normalize_key_partial = partial(
        normalize_key,
        hyphenate=hyphenate,
        camelcase=camelcase,
        default_hyphenate=default_hyphenate,
        default_camelcase=default_camelcase,
    )
    for key, value in arguments.items():
        result[normalize_key_partial(key)] = value

    if processors is None:
        processors = {}
    for key, processor in processors.items():
        try:
            normalized_key = normalize_key_partial(key)
            result[normalized_key] = processor(result[normalized_key])
        except KeyError:
            pass
    return result
