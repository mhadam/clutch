from typing import Mapping, Sequence, List, Union, Callable, cast

from clutch.method.convert.response.shared import (
    convert_response_arguments,
    convert_key,
)
from clutch.method.typing.torrent.accessor import (
    TorrentAccessorResponse,
    TorrentAccessorResponseObject,
)
from clutch.method.typing.torrent.add import TorrentAddResponse
from clutch.method.typing.torrent.mutator import TorrentMutatorArguments
from clutch.network.rpc.typing import FlatTrackerReplaceArg, TrackerReplace


def convert_accessor_response(
    arguments: TorrentAccessorResponse,
) -> TorrentAccessorResponse:
    torrents_value = arguments["torrents"]
    if isinstance(torrents_value, list) and len(torrents_value) >= 1:

        def convert_array(array):
            return [convert_response_arguments(obj) for obj in array]

        processors: Mapping[str, Callable] = {
            "trackers": convert_array,
            "trackers_stats": convert_array,
            "files": convert_array,
            "file_stats": convert_array,
            "peers": convert_array,
            "peers_from": convert_response_arguments,
        }
        # this will be effectively dead code until version 3.0 is released - it's been in the process *for years*
        if isinstance(torrents_value[0], list):
            arguments["torrents"] = process_torrent_lists(torrents_value, processors)
        elif isinstance(torrents_value[0], dict):
            arguments["torrents"] = process_torrent_objects(torrents_value, processors)
        return arguments
    return arguments


def process_torrent_lists(
    torrents_value: List[List], processors: Mapping[str, Callable]
) -> TorrentAccessorResponse:
    names: Sequence[str] = torrents_value[0]
    converted_names: List[str] = []
    for name_index, name in enumerate(names):
        converted_names.append(convert_key(name))
    torrents_value[0] = converted_names

    for line_index, line in enumerate(torrents_value[1:], 1):
        if len(line) != len(processors):
            continue
        else:
            for member_index, (member, processor_name) in enumerate(zip(line, names)):
                try:
                    torrents_value[line_index][member_index] = processors[
                        processor_name
                    ](member)
                except KeyError:
                    pass
    return cast(TorrentAccessorResponse, torrents_value)


def process_torrent_objects(
    torrents_value: Sequence[Mapping[str, object]], processors: Mapping[str, Callable]
) -> TorrentAccessorResponse:
    result: List[Mapping[str, object]] = []
    for torrent in torrents_value:
        new_torrent = {}
        for (key, value) in torrent.items():
            converted_key = convert_key(key)
            try:
                new_torrent[converted_key] = processors[converted_key](value)
            except KeyError:
                new_torrent[converted_key] = value
            except AttributeError as e:
                print(e)
        result.append(new_torrent)
    return cast(TorrentAccessorResponse, result)


def convert_add_response(arguments: Mapping[str, object]) -> TorrentAddResponse:
    return convert_response_arguments(
        arguments,
        processors={
            "torrent_added": convert_response_arguments,
            "torrent_duplicated": convert_response_arguments,
        },
    )
