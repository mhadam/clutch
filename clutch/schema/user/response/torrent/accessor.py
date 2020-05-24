from typing import Sequence, Optional, Union

from pydantic import BaseModel

from clutch.schema.user.method.torrent.accessor import TorrentAccessorField


class File(BaseModel):
    bytes_completed: int
    length: int
    name: str


class FileStats(BaseModel):
    bytes_completed: int
    wanted: bool
    priority: int


class Peer(BaseModel):
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


class PeersFrom(BaseModel):
    from_cache: int
    from_dht: int
    from_incoming: int
    from_lpd: int
    from_ltep: int
    from_pex: int
    from_tracker: int


class Tracker(BaseModel):
    announce: str
    id: int
    scrape: str
    tier: int


class TrackerStat(BaseModel):
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


class TorrentAccessorObject(BaseModel):
    activity_date: Optional[int]
    added_date: Optional[int]
    bandwidth_priority: Optional[int]
    comment: Optional[str]
    corrupt_ever: Optional[int]
    creator: Optional[str]
    date_created: Optional[int]
    desired_available: Optional[int]
    done_date: Optional[int]
    download_dir: Optional[str]
    downloaded_ever: Optional[int]
    download_limit: Optional[int]
    download_limited: Optional[bool]
    edit_date: Optional[int]
    error: Optional[int]
    error_string: Optional[str]
    eta: Optional[int]
    eta_idle: Optional[int]
    files: Optional[Sequence[File]]
    file_stats: Optional[Sequence[FileStats]]
    hash_string: Optional[str]
    have_unchecked: Optional[int]
    have_valid: Optional[int]
    honors_session_limits: Optional[bool]
    id: Optional[int]
    is_finished: Optional[bool]
    is_private: Optional[bool]
    is_stalled: Optional[bool]
    labels: Optional[Sequence[str]]
    left_until_done: Optional[int]
    magnet_link: Optional[str]
    manual_announce_time: Optional[int]
    max_connected_peers: Optional[int]
    metadata_percent_complete: Optional[float]
    name: Optional[str]
    peer_limit: Optional[int]
    peers: Optional[Sequence[Peer]]
    peers_connected: Optional[int]
    peers_from: Optional[PeersFrom]
    peers_getting_from_us: Optional[int]
    peers_sending_to_us: Optional[int]
    percent_done: Optional[float]
    pieces: Optional[str]
    piece_count: Optional[int]
    piece_size: Optional[int]
    priorities: Optional[Sequence[int]]
    queue_position: Optional[int]
    rate_download: Optional[int]
    rate_upload: Optional[int]
    recheck_progress: Optional[float]
    seconds_downloading: Optional[int]
    seconds_seeding: Optional[int]
    seed_idle_limit: Optional[int]
    seed_idle_mode: Optional[int]
    seed_ratio_limit: Optional[float]
    seed_ratio_mode: Optional[int]
    size_when_done: Optional[int]
    start_date: Optional[int]
    status: Optional[int]
    trackers: Optional[Sequence[Tracker]]
    tracker_stats: Optional[Sequence[TrackerStat]]
    total_size: Optional[int]
    torrent_file: Optional[str]
    uploaded_ever: Optional[int]
    upload_limit: Optional[int]
    upload_limited: Optional[bool]
    upload_ratio: Optional[float]
    wanted: Optional[Sequence[bool]]
    webseeds: Optional[Sequence[str]]
    webseeds_sending_to_us: Optional[int]


TorrentAccessorHeader = Sequence[TorrentAccessorField]


TorrentAccessorTable = Union[Sequence, TorrentAccessorHeader]


class TorrentAccessorResponse(BaseModel):
    removed: Optional[Sequence[int]]
    torrents: Union[Sequence[TorrentAccessorObject], Sequence[TorrentAccessorTable]]
