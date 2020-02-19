from typing import TypedDict, Literal, Sequence, Union

from clutch.network.rpc.torrent.action import IdsArg


class TorrentRemoveArgumentsOptional(TypedDict, total=False):
    delete_local_data: bool


class TorrentRemoveArguments(TorrentRemoveArgumentsOptional):
    ids: IdsArg


class TorrentRemoveOptional(TypedDict, total=False):
    tag: int


class TorrentRemove(TorrentRemoveOptional):
    method: Literal["torrent-remove"]
    arguments: TorrentRemoveArguments
