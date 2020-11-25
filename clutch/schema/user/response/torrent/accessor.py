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
    peers_from: PeersFrom
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
    total_size: int
    torrent_file: str
    uploaded_ever: int
    upload_limit: int
    upload_limited: bool
    upload_ratio: float
    wanted: Sequence[bool]
    webseeds: Sequence[str]
    webseeds_sending_to_us: int


TorrentAccessorHeader = Sequence[TorrentAccessorField]


TorrentAccessorTable = Union[Sequence, TorrentAccessorHeader]


class TorrentAccessorResponse(BaseModel):
    removed: Optional[Sequence[int]]
    torrents: Union[Sequence[TorrentAccessorObject], Sequence[TorrentAccessorTable]]
