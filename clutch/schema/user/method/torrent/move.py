from clutch.compat import TypedDict

from clutch.schema.user.method.shared import IdsArg


class TorrentMoveArgumentsOptional(TypedDict, total=False):
    move: bool


class TorrentMoveArguments(TorrentMoveArgumentsOptional):
    ids: IdsArg
    location: str
