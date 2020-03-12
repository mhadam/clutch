from typing import TypedDict, Literal

from clutch.method.typing.torrent.action import IdsArg


class TorrentMoveArgumentsOptional(TypedDict, total=False):
    move: bool


class TorrentMoveArguments(TorrentMoveArgumentsOptional):
    ids: IdsArg
    location: str


class TorrentMoveOptional(TypedDict, total=False):
    tag: int


class TorrentMove(TorrentMoveOptional):
    method: Literal["torrent-set-location"]
    arguments: TorrentMoveArguments
