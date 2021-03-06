from clutch.compat import Literal


SessionAccessorField = Literal[
    "alt_speed_down",
    "alt_speed_enabled",
    "alt_speed_time_begin",
    "alt_speed_time_enabled",
    "alt_speed_time_end",
    "alt_speed_time_day",
    "alt_speed_up",
    "blocklist_url",
    "blocklist_size",
    "blocklist_enabled",
    "cache_size_mb",
    "config_dir",
    "download_dir",
    "download_queue_size",
    "download_queue_enabled",
    "dht_enabled",
    "encryption",
    "idle_seeding_limit",
    "idle_seeding_limit_enabled",
    "incomplete_dir",
    "incomplete_dir_enabled",
    "lpd_enabled",
    "peer_limit_global",
    "peer_limit_per_torrent",
    "pex_enabled",
    "peer_port",
    "peer_port_random_on_start",
    "port_forwarding_enabled",
    "queue_stalled_enabled",
    "queue_stalled_minutes",
    "rename_partial_files",
    "rpc_version",
    "rpc_version_minimum",
    "script_torrent_done_filename",
    "script_torrent_done_enabled",
    "seed_ratio_limit",
    "seed_ratio_limited",
    "seed_queue_size",
    "seed_queue_enabled",
    "session_id",
    "speed_limit_down",
    "speed_limit_down_enabled",
    "speed_limit_up",
    "speed_limit_up_enabled",
    "start_added_torrents",
    "trash_original_torrent_files",
    "units",
    "utp_enabled",
    "version",
]
