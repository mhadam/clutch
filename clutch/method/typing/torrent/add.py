from dataclasses import dataclass
from typing import TypedDict, Literal, Sequence, Union


@dataclass
class Cookie:
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


class Torrent(TypedDict):
    id: int
    name: str
    hash_string: str


class TorrentAddedResponse(TypedDict):
    torrent_added: Torrent


class TorrentDuplicateResponse(TypedDict):
    torrent_duplicated: Torrent


TorrentAddResponse = Union[TorrentAddedResponse, TorrentDuplicateResponse]
