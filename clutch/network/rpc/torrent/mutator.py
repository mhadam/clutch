from typing import TypedDict, Literal, Sequence

from clutch.network.rpc.typing import TrackerReplace


class TorrentMutatorArguments(TypedDict, total=False):
    bandwidth_priority: int
    download_limit: int
    download_limited: bool
    files_wanted: Sequence[str]
    files_unwanted: Sequence[str]
    honors_session_limits: bool
    labels: Sequence[str]
    location: str
    peer_limit: int
    priority_high: Sequence[str]
    priority_low: Sequence[str]
    priority_normal: Sequence[str]
    queue_position: int
    seed_idle_limit: int
    seed_idle_mode: int
    seed_ratio_limit: float
    seed_ratio_mode: int
    tracker_add: Sequence[str]
    tracker_remove: Sequence[str]
    # tracker_replace requires conversion, otherwise we need a strange typing
    # oddly doesn't mirror ids (only int appears to be accepted vs. hash]
    tracker_replace: Sequence[TrackerReplace]
    upload_limit: int
    upload_limited: bool


class TorrentMutatorRequired(TypedDict):
    method: Literal["torrent-set"]


class TorrentMutator(TorrentMutatorRequired, total=False):
    arguments: TorrentMutatorArguments
    tag: int
