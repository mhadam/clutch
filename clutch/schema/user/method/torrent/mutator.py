from typing import NewType, Sequence, TypedDict

from clutch.schema.user.method.shared import IdsArg

Url = NewType("Url", str)


class TorrentMutatorArguments(TypedDict, total=False):
    bandwidth_priority: int
    download_limit: int
    download_limited: bool
    files_wanted: Sequence[int]  # empty is shorthand for all
    files_unwanted: Sequence[int]  # empty is shorthand for all
    group: str
    honors_session_limits: bool
    ids: IdsArg
    labels: Sequence[str]
    location: str
    peer_limit: int
    priority_high: Sequence[int]  # empty is shorthand for all
    priority_low: Sequence[int]  # empty is shorthand for all
    priority_normal: Sequence[int]  # empty is shorthand for all
    queue_position: int
    seed_idle_limit: int
    seed_idle_mode: int
    seed_ratio_limit: float
    seed_ratio_mode: int
    sequential_download: bool
    tracker_list: Sequence[Sequence[Url]]
    upload_limit: int
    upload_limited: bool
