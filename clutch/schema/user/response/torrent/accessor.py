from enum import Enum, unique
from typing import Sequence, Union

from pydantic import BaseModel

from clutch.schema.user.method.torrent.accessor import TorrentAccessorField


@unique
class Status(Enum):
    STOPPED = 0  # Torrent is stopped
    CHECK_WAIT = 1  # Torrent is queued to verify local data
    CHECK = 2  # Torrent is verifying local data
    DOWNLOAD_WAIT = 3  # Torrent is queued to download
    DOWNLOAD = 4  # Torrent is downloading
    SEED_WAIT = 5  # Torrent is queued to seed
    SEED = 6  # Torrent is seeding


class File(BaseModel):
    bytes_completed: int
    length: int
    name: str
    begin_piece: int
    end_piece: int


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
    rate_to_client: int  # B/s
    rate_to_peer: int  # B/s


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
    sitename: str
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
    sitename: str
    tier: int


class TorrentAccessorObject(BaseModel):
    activity_date: int | None = None
    added_date: int | None = None
    availability: list[int] | None = (
        None  # An array of `pieceCount` numbers representing the number of
    )
    # connected peers that have each piece, or -1 if we already have the piece ourselves.
    bandwidth_priority: int | None = None
    comment: str | None = None
    corrupt_ever: int | None = None
    creator: str | None = None
    date_created: int | None = None
    desired_available: int | None = None
    done_date: int | None = None
    download_dir: str | None = None
    downloaded_ever: int | None = None
    download_limit: int | None = None
    download_limited: bool | None = None
    edit_date: int | None = None
    error: int | None = None
    error_string: str | None = None
    eta: int | None = None
    eta_idle: int | None = None
    file_count: int | None = None
    files: Sequence[File] | None = None
    file_stats: Sequence[FileStats] | None = None
    group: str | None = None
    hash_string: str | None = None
    have_unchecked: int | None = None
    have_valid: int | None = None
    honors_session_limits: bool | None = None
    id: int | None = None
    is_finished: bool | None = None
    is_private: bool | None = None
    is_stalled: bool | None = None
    labels: Sequence[str] | None = None
    left_until_done: int | None = None
    magnet_link: str | None = None
    manual_announce_time: int | None = None
    max_connected_peers: int | None = None
    metadata_percent_complete: float | None = None
    name: str | None = None
    peer_limit: int | None = None
    peers: Sequence[Peer] | None = None
    peers_connected: int | None = None
    peers_from: PeersFrom | None = None
    peers_getting_from_us: int | None = None
    peers_sending_to_us: int | None = None
    percent_complete: float | None = None
    percent_done: float | None = None
    pieces: str | None = None
    piece_count: int | None = None
    piece_size: int | None = None
    priorities: Sequence[int] | None = None
    primary_mime_type: str | None = None
    queue_position: int | None = None
    rate_download: int | None = None
    rate_upload: int | None = None
    recheck_progress: float | None = None
    seconds_downloading: int | None = None
    seconds_seeding: int | None = None
    seed_idle_limit: int | None = None
    seed_idle_mode: int | None = None
    seed_ratio_limit: float | None = None
    seed_ratio_mode: int | None = None
    sequential_download: bool | None = None
    size_when_done: int | None = None
    start_date: int | None = None
    status: Status | None = None
    trackers: Sequence[Tracker] | None = None
    tracker_list: str | None = (
        None  # string of announce URLs, one per line, with a blank line between tiers
    )
    tracker_stats: Sequence[TrackerStat] | None = None
    total_size: int | None = None
    torrent_file: str | None = None
    uploaded_ever: int | None = None
    upload_limit: int | None = None
    upload_limited: bool | None = None
    upload_ratio: float | None = None
    wanted: Sequence[bool] | None = (
        None  # An array of `tr_torrentFileCount()` 0/1, 1 (true) if the corresponding file is to be downloaded.
    )
    webseeds: Sequence[str] | None = None
    webseeds_sending_to_us: int | None = None


TorrentAccessorHeader = Sequence[TorrentAccessorField]


TorrentAccessorTable = Union[Sequence, TorrentAccessorHeader]


class TorrentAccessorResponse(BaseModel):
    removed: Sequence[int] | None = None
    torrents: (
        Union[Sequence[TorrentAccessorObject], Sequence[TorrentAccessorTable]] | None
    ) = None
