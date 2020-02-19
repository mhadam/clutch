from typing import TypedDict, Literal, Sequence, Union

from clutch.network.rpc.torrent.action import IdsArg


class TorrentMoveArgumentsOptional(TypedDict, total=False):
    move: bool


class TorrentMoveArguments(TorrentMoveArgumentsOptional):
    ids: IdsArg
    location: str


class TorrentMoveOptional(TypedDict, total=False):
    tag: int


class TorrentMove(TorrentMoveOptional):
    method: Literal["torrent-move"]
    arguments: TorrentMoveArguments
