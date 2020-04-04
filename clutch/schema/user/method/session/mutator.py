from clutch.compat import TypedDict

from clutch.schema.user.method.session.shared import Units


class SessionMutatorArguments(TypedDict, total=False):
    alt_speed_down: int
    alt_speed_enabled: bool
    alt_speed_time_begin: int
    alt_speed_time_enabled: bool
    alt_speed_time_end: int
    alt_speed_time_day: int
    alt_speed_up: int
    blocklist_url: str
    blocklist_enabled: bool
    cache_size_mb: int
    download_dir: str
    download_queue_size: int
    download_queue_enabled: bool
    dht_enabled: bool
    encryption: str
    idle_seeding_limit: int
    idle_seeding_limit_enabled: bool
    incomplete_dir: str
    incomplete_dir_enabled: bool
    lpd_enabled: bool
    peer_limit_global: int
    peer_limit_per_torrent: int
    pex_enabled: bool
    peer_port: int
    peer_port_random_on_start: bool
    port_forwarding_enabled: bool
    queue_stalled_enabled: bool
    queue_stalled_minutes: int
    rename_partial_files: bool
    script_torrent_done_filename: str
    script_torrent_done_enabled: bool
    seed_ratio_limit: float
    seed_ratio_limited: bool
    seed_queue_size: int
    seed_queue_enabled: bool
    speed_limit_down: int
    speed_limit_down_enabled: bool
    speed_limit_up: int
    speed_limit_up_enabled: bool
    start_added_torrents: bool
    trash_original_torrent_files: bool
    units: Units
    utp_enabled: bool
