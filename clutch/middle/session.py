from typing import Dict, Any, Mapping, Sequence

from clutch.network.rpc.message import Request
from clutch.network.rpc.session.accessor import SessionAccessor
from clutch.network.rpc.session.mutator import SessionMutatorArguments, SessionMutator
from clutch.network.rpc.session.shared import SessionArguments


hyphenated_arguments: Sequence[str] = [
    'files-wanted',
    'files-unwanted',
    'peer-limit',
    'priority-high',
    'priority-low',
    'priority-normal'
]


def _convert(key: str) -> str:
    hyphenated = key.replace("_", "-")
    if hyphenated in hyphenated_arguments:
        words = hyphenated.split("-")
        for word in words[1:]:
            word.capitalize()
        return "-".join(words)
    else:
        words = hyphenated.split("-")
        for word in words[1:]:
            word.capitalize()
        return "".join(words)


def _clone_and_convert_keys(arguments: Mapping[str, Any]) -> Dict[str, Any]:
    result = dict(arguments)
    for (k, v) in arguments.items():
        result[_convert(k)] = v
    return result


def convert_mutator(mutator: SessionMutator) -> Request:
    def process_arguments(args: SessionMutatorArguments) -> Mapping[str, str]:
        result = _clone_and_convert_keys(args)
        for (k, v) in result.items():
            result[k] = str(v)
        return result

    request = Request(method=mutator['method'])
    if len(arguments := mutator["arguments"]) > 0:
        request['arguments'] = process_arguments(arguments)

    try:
        request['tag'] = mutator['tag']
    except KeyError:
        pass
    return request



def convert_accessor(accessor: SessionAccessor) -> Request:
    def process_arguments(args: SessionArguments) -> Mapping[str, str]:
        result = _clone_and_convert_keys(args)
        for (k, v) in result.items():
            result[k] = str(v)
        return result

    request = Request(method=accessor['method'])
    if len(arguments := accessor["arguments"]) > 0:
        request['arguments'] = process_arguments(arguments)

    try:
        request['tag'] = accessor['tag']
    except KeyError:
        pass
    return request
