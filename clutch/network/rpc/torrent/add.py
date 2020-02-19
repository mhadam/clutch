from typing import TypedDict, Literal, Sequence, Union


class TorrentAddArgumentsOptional(TypedDict, total=False):
    cookies: str
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


class TorrentAddOptional(TypedDict, total=False):
    tag: int


class TorrentAdd(TorrentAddOptional):
    method: Literal["torrent-add"]
    arguments: TorrentAddArguments
