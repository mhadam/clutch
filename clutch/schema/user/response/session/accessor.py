from typing import Tuple, Union, Optional

from pydantic import BaseModel

from clutch.compat import Literal

BinaryDataRateUnits = Tuple[
    Literal["KiB/s"], Literal["MiB/s"], Literal["GiB/s"], Literal["TiB/s"]
]
DecimalDataRateUnits = Tuple[
    Literal["kB/s", "KB/s"], Literal["MB/s"], Literal["GB/s"], Literal["TB/s"]
]
DataRateUnits = Union[BinaryDataRateUnits, DecimalDataRateUnits]

BinaryDataSizeUnits = Tuple[
    Literal["KiB"], Literal["MiB"], Literal["GiB"], Literal["TiB"]
]
DecimalDataSizeUnits = Tuple[
    Literal["kB", "KB"], Literal["MB"], Literal["GB"], Literal["TB"]
]
DataSizeUnits = Union[BinaryDataSizeUnits, DecimalDataSizeUnits]

ByteDefinition = Literal[1000, 1024]


class Units(BaseModel):
    speed_units: DataRateUnits
    speed_bytes: ByteDefinition
    size_units: DataSizeUnits
    size_bytes: ByteDefinition
    memory_units: DataSizeUnits
    memory_bytes: ByteDefinition


class SessionAccessor(BaseModel):
    alt_speed_down: int
    alt_speed_enabled: bool
    alt_speed_time_begin: int
    alt_speed_time_enabled: bool
    alt_speed_time_end: int
    alt_speed_time_day: int
    alt_speed_up: int
    blocklist_url: str
    blocklist_size: int
    blocklist_enabled: bool
    cache_size_mb: int
    config_dir: str
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
    rpc_version: int
    rpc_version_minimum: int
    script_torrent_done_filename: str
    script_torrent_done_enabled: bool
    seed_ratio_limit: float
    seed_ratio_limited: bool
    seed_queue_size: int
    seed_queue_enabled: bool
    session_id: Optional[str]
    speed_limit_down: int
    speed_limit_down_enabled: bool
    speed_limit_up: int
    speed_limit_up_enabled: bool
    start_added_torrents: bool
    trash_original_torrent_files: bool
    units: Units
    utp_enabled: bool
    version: str
