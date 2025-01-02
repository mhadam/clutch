from enum import Enum, unique


@unique
class TorrentActionMethod(Enum):
    START = "torrent-start"
    START_NOW = "torrent-start-now"
    STOP = "torrent-stop"
    VERIFY = "torrent-verify"
    REANNOUNCE = "torrent-reannounce"
