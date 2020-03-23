from typing import TypedDict, Literal, Set, Sequence, Union, Mapping

from clutch.method.typing.torrent.action import IdsArg

AccessorField = Literal[
    "activity_date",
    "added_date",
    "bandwidth_priority",
    "comment",
    "corrupt_ever",
    "creator",
    "date_created",
    "desired_available",
    "done_date",
    "download_dir",
    "downloaded_ever",
    "download_limit",
    "download_limited",
    "edit_date",
    "error",
    "error_string",
    "eta",
    "eta_idle",
    "files",
    "file_stats",
    "hash_string",
    "have_unchecked",
    "have_valid",
    "honors_session_limits",
    "id",
    "is_finished",
    "is_private",
    "is_stalled",
    "labels",
    "left_until_done",
    "magnet_link",
    "manual_announce_time",
    "max_connected_peers",
    "metadata_percent_complete",
    "name",
    "peer_limit",
    "peers",
    "peers_connected",
    "peers_from",
    "peers_getting_from_us",
    "peers_sending_to_us",
    "percent_done",
    "pieces",
    "piece_count",
    "piece_size",
    "priorities",
    "queue_position",
    "rate_download",
    "rate_upload",
    "recheck_progress",
    "seconds_downloading",
    "seconds_seeding",
    "seed_idle_limit",
    "seed_idle_mode",
    "seed_ratio_limit",
    "seed_ratio_mode",
    "size_when_done",
    "start_date",
    "status",
    "trackers",
    "tracker_stats",
    "total_size",
    "torrent_file",
    "uploaded_ever",
    "upload_limit",
    "upload_limited",
    "upload_ratio",
    "wanted",
    "webseeds",
    "webseeds_sending_to_us",
]

TorrentAccessorFields = Set[AccessorField]


class TorrentAccessorArgumentsRequired(TypedDict):
    fields: TorrentAccessorFields


class TorrentAccessorArguments(TorrentAccessorArgumentsRequired, total=False):
    ids: IdsArg
    format: Literal["objects", "table"]


class File(TypedDict):
    bytes_completed: int
    length: int
    name: str


class FileStats(TypedDict):
    bytes_completed: int
    wanted: bool
    priority: int


class Peer(TypedDict):
    address: str
    client_name: str
    client_is_choked: bool
    client_is_interested: bool
    flag_str: str
    is_downloading_from: bool
    is_encrypted: bool
    is_incoming: bool
    is_uploading_to: bool
    is_utp: bool
    peer_is_choked: bool
    peer_is_interested: bool
    port: int
    progress: float
    rate_to_client: int
    rate_to_peer: int


class Tracker(TypedDict):
    announce: str
    id: int
    scrape: str
    tier: int


class TrackerStat(TypedDict):
    announce: str
    announce_state: int
    download_count: int
    has_announced: bool
    has_scraped: bool
    host: str
    id: int
    is_backup: bool
    last_announce_peer_count: int
    last_announce_result: str
    last_announce_start_time: int
    last_announce_succeeded: bool
    last_announce_time: int
    last_announce_timed_out: bool
    last_scrape_result: str
    last_scrape_start_time: int
    last_scrape_succeeded: bool
    last_scrape_time: int
    last_scrape_timed_out: bool
    leecher_count: int
    next_announce_time: int
    next_scrape_time: int
    scrape: str
    scrape_state: int
    seeder_count: int
    tier: int


class TorrentAccessorResponseObject(TypedDict, total=False):
    activity_date: int
    added_date: int
    bandwidth_priority: int
    comment: str
    corrupt_ever: int
    creator: str
    date_created: int
    desired_available: int
    done_date: int
    download_dir: str
    downloaded_ever: int
    download_limit: int
    download_limited: bool
    edit_date: int
    error: int
    error_string: str
    eta: int
    eta_idle: int
    files: Sequence[File]
    file_stats: Sequence[FileStats]
    hash_string: str
    have_unchecked: int
    have_valid: int
    honors_session_limits: bool
    id: int
    is_finished: bool
    is_private: bool
    is_stalled: bool
    labels: Sequence[str]
    left_until_done: int
    magnet_link: str
    manual_announce_time: int
    max_connected_peers: int
    metadata_percent_complete: float
    name: str
    peer_limit: int
    peers: Sequence[Peer]
    peers_connected: int
    peers_from: object
    peers_getting_from_us: int
    peers_sending_to_us: int
    percent_done: float
    pieces: str
    piece_count: int
    piece_size: int
    priorities: Sequence[int]
    queue_position: int
    rate_download: int
    rate_upload: int
    recheck_progress: float
    seconds_downloading: int
    seconds_seeding: int
    seed_idle_limit: int
    seed_idle_mode: int
    seed_ratio_limit: float
    seed_ratio_mode: int
    size_when_done: int
    start_date: int
    status: int
    trackers: Sequence[Tracker]
    tracker_stats: Sequence[TrackerStat]
    total_Size: int
    torrent_File: str
    uploaded_ever: int
    upload_limit: int
    upload_limited: bool
    upload_ratio: float
    wanted: Sequence[bool]
    webseeds: Sequence[str]
    webseeds_sending_to_us: int


class TorrentAccessorResponseOptional(TypedDict, total=False):
    removed: Sequence[int]


class TorrentAccessorResponse(TorrentAccessorResponseOptional):
    torrents: Union[
        Sequence[Mapping[str, object]],
        Sequence[Sequence[TorrentAccessorResponseObject]],
    ]


field_keys: Sequence[str] = [
    "activity_date",
    "added_date",
    "bandwidth_priority",
    "comment",
    "corrupt_ever",
    "creator",
    "date_created",
    "desired_available",
    "done_date",
    "download_dir",
    "downloaded_ever",
    "download_limit",
    "download_limited",
    "edit_date",
    "error",
    "error_string",
    "eta",
    "eta_idle",
    "files",
    "file_stats",
    "hash_string",
    "have_unchecked",
    "have_valid",
    "honors_session_limits",
    "id",
    "is_finished",
    "is_private",
    "is_stalled",
    "labels",
    "left_until_done",
    "magnet_link",
    "manual_announce_time",
    "max_connected_peers",
    "metadata_percent_complete",
    "name",
    "peer_limit",
    "peers",
    "peers_connected",
    "peers_from",
    "peers_getting_from_us",
    "peers_sending_to_us",
    "percent_done",
    "pieces",
    "piece_count",
    "piece_size",
    "priorities",
    "queue_position",
    "rate_download",
    "rate_upload",
    "recheck_progress",
    "seconds_downloading",
    "seconds_seeding",
    "seed_idle_limit",
    "seed_idle_mode",
    "seed_ratio_limit",
    "seed_ratio_mode",
    "size_when_done",
    "start_date",
    "status",
    "trackers",
    "tracker_stats",
    "total_size",
    "torrent_file",
    "uploaded_ever",
    "upload_limit",
    "upload_limited",
    "upload_ratio",
    "wanted",
    "webseeds",
    "webseeds_sending_to_us",
]
