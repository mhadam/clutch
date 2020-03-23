from enum import unique, Enum
from typing import TypedDict, Union, Sequence, Literal

IdsArg = Union[int, Sequence[Union[str, int]], Literal["recently_active"]]


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
