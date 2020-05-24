from typing import Sequence

from clutch.compat import TypedDict
from clutch.schema.user.method.shared import IdsArg


class TrackerReplace(TypedDict):
    tracker_id: int
    announce_url: str


class TorrentMutatorArguments(TypedDict, total=False):
    bandwidth_priority: int
    download_limit: int
    download_limited: bool
    edit_date: int
    files_wanted: Sequence[str]  # empty is shorthand for all
    files_unwanted: Sequence[str]  # empty is shorthand for all
    honors_session_limits: bool
    ids: IdsArg
    labels: Sequence[str]
    location: str
    peer_limit: int
    priority_high: Sequence[str]  # empty is shorthand for all
    priority_low: Sequence[str]  # empty is shorthand for all
    priority_normal: Sequence[str]  # empty is shorthand for all
    queue_position: int
    seed_idle_limit: int
    seed_idle_mode: int
    seed_ratio_limit: float
    seed_ratio_mode: int
    tracker_add: Sequence[str]
    tracker_remove: Sequence[str]
    tracker_replace: Sequence[TrackerReplace]
    upload_limit: int
    upload_limited: bool
