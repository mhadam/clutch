from typing import TypedDict, Literal, Set

from clutch.network.rpc.torrent.action import IdsArg

AccessorField = Literal[
    "activity-date",
    "added-date",
    "bandwidth-priority",
    "comment",
    "corrupt-ever",
    "creator",
    "date-created",
    "desired-available",
    "done-date",
    "download-dir",
    "downloaded-ever",
    "download-limit",
    "download-limited",
    "edit-date",
    "error",
    "error-string",
    "eta",
    "eta-idle",
    "files",
    "file-stats",
    "hash-string",
    "have-unchecked",
    "have-valid",
    "honors-session-limits",
    "id",
    "is-finished",
    "is-private",
    "is-stalled",
    "labels",
    "left-until-done",
    "magnet-link",
    "manual-announce-time",
    "max-connected-peers",
    "metadata-percent-complete",
    "name",
    "peer-limit",
    "peers",
    "peers-connected",
    "peers-from",
    "peers-getting-from-us",
    "peers-sending-to-us",
    "percent-done",
    "pieces",
    "piece-count",
    "piece-size",
    "priorities",
    "queue-position",
    "rate-download",
    "rate-upload",
    "recheck-progress",
    "seconds-downloading",
    "seconds-seeding",
    "seed-idle-limit",
    "seed-idle-mode",
    "seed-ratio-limit",
    "seed-ratio-mode",
    "size-when-done",
    "start-date",
    "status",
    "trackers",
    "tracker-stats",
    "total-size",
    "torrent-file",
    "uploaded-ever",
    "upload-limit",
    "upload-limited",
    "upload-ratio",
    "wanted",
    "webseeds",
    "webseeds-sending-to-us",
]

TorrentAccessorFields = Set[AccessorField]


class TorrentAccessorArgumentsRequired(TypedDict):
    fields: TorrentAccessorFields


class TorrentAccessorArguments(TorrentAccessorArgumentsRequired, total=False):
    ids: IdsArg


class TorrentAccessorMethod(TypedDict):
    method: Literal["torrent-get"]


class TorrentAccessor(TorrentAccessorMethod, total=False):
    arguments: TorrentAccessorArguments
    tag: int
