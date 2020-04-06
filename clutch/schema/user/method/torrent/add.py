from typing import Sequence, Union

from clutch.compat import TypedDict


class Cookie(TypedDict):
    name: str
    content: str


class TorrentAddArgumentsOptional(TypedDict, total=False):
    cookies: Sequence[Cookie]
    download_dir: str
    paused: bool
    peer_limit: int
    bandwidth_priority: int
    files_wanted: Sequence[int]
    files_unwanted: Sequence[int]
    priority_high: Sequence[int]
    priority_low: Sequence[int]
    priority_normal: Sequence[int]


class TorrentAddByFilenameArguments(TorrentAddArgumentsOptional):
    filename: str


class TorrentAddByMetainfoArguments(TorrentAddArgumentsOptional):
    metainfo: str


TorrentAddArguments = Union[
    TorrentAddByFilenameArguments, TorrentAddByMetainfoArguments
]
