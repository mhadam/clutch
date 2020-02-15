from enum import Enum, unique


@unique
class Mutators(Enum):
    TORRENT_SET = "torrent_set"


@unique
class Accessors(Enum):
    TORRENT_GET = "torrent-get"


@unique
class TorrentMethod(Enum):
    TORRENT_ADD = "torrent-add"
    TORRENT_REMOVE = "torrent-remove"
    TORRENT_SET_LOCATION = "torrent-set-location"
    TORRENT_RENAME_PATH = "torrent-rename-path"


@unique
class SessionMethod(Enum):
    SESSION_SET = "session-set"
    SESSION_GET = "session-get"
    SESSION_STATS = "session-stats"
    SESSION_SHUTDOWN = "session-close"


@unique
class OtherMethod(Enum):
    BLOCKLIST_UPDATE = "blocklist-update"
    PORT_TEST = "port-test"
    FREE_SPACE = "free-space"


@unique
class QueueMethod(Enum):
    QUEUE_MOVE_TOP = "queue-move-top"
    QUEUE_MOVE_UP = "queue-move-up"
    QUEUE_MOVE_DOWN = "queue-move-down"
    QUEUE_MOVE_BOTTOM = "queue-move-bottom"
