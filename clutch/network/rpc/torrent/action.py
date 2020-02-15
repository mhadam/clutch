from enum import unique, Enum
from typing import TypedDict

from clutch.network.rpc.typing import IdsArg


@unique
class TorrentActionMethod(Enum):
    START = "torrent-start"
    START_NOW = "torrent-start-now"
    STOP = "torrent-stop"
    VERIFY = "torrent-verify"
    REANNOUNCE = "torrent-reannounce"


class TorrentActionArguments(TypedDict):
    ids: IdsArg


class TorrentActionRequired(TypedDict):
    method: TorrentActionMethod


class TorrentAction(TorrentActionRequired, total=False):
    arguments: TorrentActionArguments
    tag: int
