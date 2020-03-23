from typing import Mapping, Sequence, Union, List

from clutch.method.convert.argument.shared import convert_arguments, normalize_key
from clutch.method.typing.torrent.accessor import TorrentAccessorArguments
from clutch.method.typing.torrent.add import TorrentAddArguments
from clutch.method.typing.torrent.mutator import TorrentMutatorArguments
from clutch.method.typing.torrent.remove import TorrentRemoveArguments
from clutch.network.rpc.typing import FlatTrackerReplaceArg, TrackerReplace


def convert_mutator(arguments: TorrentMutatorArguments) -> Mapping[str, object]:
    def flatten(tuples: Sequence[TrackerReplace]) -> FlatTrackerReplaceArg:
        result: List[Union[int, str]] = []
        pair: TrackerReplace
        for pair in tuples:
            result.append(pair.trackerId)
            result.append(pair.announceUrl)
        return result

    return convert_arguments(
        arguments,
        processors={"tracker_replace": flatten},
        hyphenate=frozenset(
            {
                "files_wanted",
                "files_unwanted",
                "peer_limit",
                "priority_high",
                "priority_low",
                "priority_normal",
            }
        ),
        default_camelcase=True,
    )


def convert_accessor(arguments: TorrentAccessorArguments) -> Mapping[str, object]:
    def convert_fields(fields: Sequence[str]) -> Sequence[str]:
        result = [
            normalize_key(
                key, hyphenate=frozenset({"peer_limit"}), default_camelcase=True
            )
            for key in fields
        ]
        return result

    return convert_arguments(arguments, {"fields": convert_fields})


def convert_add(arguments: TorrentAddArguments) -> Mapping[str, object]:
    return convert_arguments(
        arguments,
        hyphenate=frozenset(
            {
                "files_wanted",
                "files_unwanted",
                "peer_limit",
                "priority_high",
                "priority_low",
                "priority_normal",
                "download_dir",
            }
        ),
    )


def convert_remove(arguments: TorrentRemoveArguments) -> Mapping[str, object]:
    return convert_arguments(arguments, default_hyphenate=True)
