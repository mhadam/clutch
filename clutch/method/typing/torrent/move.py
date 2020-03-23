from typing import TypedDict, Literal

from clutch.method.typing.torrent.action import IdsArg


class TorrentMoveArgumentsOptional(TypedDict, total=False):
    move: bool


class TorrentMoveArguments(TorrentMoveArgumentsOptional):
    ids: IdsArg
    location: str
