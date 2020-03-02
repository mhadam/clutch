from typing import Dict, Any, Mapping, Sequence, Union, List

from clutch.network.rpc.message import Request
from clutch.network.rpc.torrent.accessor import TorrentAccessor, TorrentAccessorArguments
from clutch.network.rpc.torrent.action import TorrentAction, TorrentActionArguments
from clutch.network.rpc.torrent.add import TorrentAdd, TorrentAddArguments
from clutch.network.rpc.torrent.move import TorrentMove, TorrentMoveArguments
from clutch.network.rpc.torrent.mutator import TorrentMutator, TorrentMutatorArguments
from clutch.network.rpc.torrent.remove import TorrentRemove, TorrentRemoveArguments
from clutch.network.rpc.torrent.rename import TorrentRename, TorrentRenameArguments
from clutch.network.rpc.typing import FlatTrackerReplaceArg, TrackerReplace

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


def convert_action(action: TorrentAction) -> Request:
    def process_arguments(args: TorrentActionArguments) -> Mapping[str, str]:
        result = _clone_and_convert_keys(args)
        for (k, v) in result.items():
            result[k] = str(v)
        return result

    request = Request(method=action['method'].value)
    if len(arguments := action["arguments"]) > 0:
        request['arguments'] = process_arguments(arguments)

    try:
        request['tag'] = action['tag']
    except KeyError:
        pass
    return request


def convert_mutator(mutator: TorrentMutator) -> Request:
    def flatten(tuples: Sequence[TrackerReplace]) -> FlatTrackerReplaceArg:
        result: List[Union[int, str]] = []
        pair: TrackerReplace
        for pair in tuples:
            result.append(pair.trackerId)
            result.append(pair.announceUrl)
        return result

    def process_arguments(args: TorrentMutatorArguments) -> Mapping[str, str]:
        result = _clone_and_convert_keys(args)
        try:
            result['tracker-replace'] = flatten(result["tracker-replace"])
        except KeyError:
            pass
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


def convert_accessor(accessor: TorrentAccessor) -> Request:
    def process_arguments(args: TorrentAccessorArguments) -> Mapping[str, str]:
        result = _clone_and_convert_keys(args)
        for (k, v) in result.items():
            if isinstance(v, set):
                result[k] = v
                continue
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


def convert_add(command: TorrentAdd) -> Request:
    def process_arguments(args: TorrentAddArguments) -> Mapping[str, str]:
        result = _clone_and_convert_keys(args)
        for (k, v) in result.items():
            if isinstance(v, set):
                result[k] = v
                continue
            result[k] = str(v)
        return result

    request = Request(method=command['method'])
    request['arguments'] = process_arguments(command['arguments'])

    try:
        request['tag'] = command['tag']
    except KeyError:
        pass
    return request


def convert_move(command: TorrentMove) -> Request:
    def process_arguments(args: TorrentMoveArguments) -> Mapping[str, str]:
        result = _clone_and_convert_keys(args)
        for (k, v) in result.items():
            if isinstance(v, set):
                result[k] = v
                continue
            result[k] = str(v)
        return result

    request = Request(method=command['method'])
    request['arguments'] = process_arguments(command['arguments'])

    try:
        request['tag'] = command['tag']
    except KeyError:
        pass
    return request


def convert_remove(command: TorrentRemove) -> Request:
    def process_arguments(args: TorrentRemoveArguments) -> Mapping[str, str]:
        result = _clone_and_convert_keys(args)
        for (k, v) in result.items():
            if isinstance(v, set):
                result[k] = v
                continue
            result[k] = str(v)
        return result

    request = Request(method=command['method'])
    request['arguments'] = process_arguments(command['arguments'])

    try:
        request['tag'] = command['tag']
    except KeyError:
        pass
    return request


def convert_rename(command: TorrentRename) -> Request:
    def process_arguments(args: TorrentRenameArguments) -> Mapping[str, str]:
        result = _clone_and_convert_keys(args)
        for (k, v) in result.items():
            if isinstance(v, set):
                result[k] = v
                continue
            result[k] = str(v)
        return result

    request = Request(method=command['method'])
    request['arguments'] = process_arguments(command['arguments'])

    try:
        request['tag'] = command['tag']
    except KeyError:
        pass
    return request
