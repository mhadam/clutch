from typing import TypedDict

from clutch.method.typing.torrent.action import IdsArg


class TorrentRemoveArgumentsOptional(TypedDict, total=False):
    delete_local_data: bool


class TorrentRemoveArguments(TorrentRemoveArgumentsOptional):
    ids: IdsArg
