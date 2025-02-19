from typing import Literal

SessionAccessorField = Literal[
    "alt_speed_down",
    "alt_speed_enabled",
    "alt_speed_time_begin",
    "alt_speed_time_day",
    "alt_speed_time_enabled",
    "alt_speed_time_end",
    "alt_speed_up",
    "blocklist_enabled",
    "blocklist_size",
    "blocklist_url",
    "cache_size_mb",
    "config_dir",
    "default_trackers",
    "dht_enabled",
    "download_dir",
    "download_queue_enabled",
    "download_queue_size",
    "encryption",
    "idle_seeding_limit_enabled",
    "idle_seeding_limit",
    "incomplete_dir_enabled",
    "incomplete_dir",
    "lpd_enabled",
    "peer_limit_global",
    "peer_limit_per_torrent",
    "peer_port_random_on_start",
    "peer_port",
    "pex_enabled",
    "port_forwarding_enabled",
    "queue_stalled_enabled",
    "queue_stalled_minutes",
    "rename_partial_files",
    "reqq",
    "rpc_version_minimum",
    "rpc_version_semver",
    "rpc_version",
    "script_torrent_added_enabled",
    "script_torrent_added_filename",
    "script_torrent_done_enabled",
    "script_torrent_done_filename",
    "script_torrent_done_seeding_enabled",
    "script_torrent_done_seeding_filename",
    "seed_queue_enabled",
    "seed_queue_size",
    "seed_ratio_limit",
    "seed_ratio_limited",
    "session_id",
    "speed_limit_down_enabled",
    "speed_limit_down",
    "speed_limit_up_enabled",
    "speed_limit_up",
    "start_added_torrents",
    "trash_original_torrent_files",
    "units",
    "utp_enabled",
    "version",
]
