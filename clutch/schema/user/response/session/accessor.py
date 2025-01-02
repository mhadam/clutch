from typing import Annotated, Any, Literal, Tuple, Union

from pydantic import AfterValidator, BaseModel

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


def validate_tiers(v: Any) -> list[list[str]]:
    if not isinstance(v, str):
        raise ValueError(f"value {v} is not a string")
    return [x.split() for x in v.split("\n\n")]


class SessionAccessor(BaseModel):
    alt_speed_down: int | None
    alt_speed_enabled: bool | None
    alt_speed_time_begin: int | None
    alt_speed_time_enabled: bool | None
    alt_speed_time_end: int | None
    alt_speed_time_day: int | None
    alt_speed_up: int | None
    blocklist_url: str | None
    blocklist_size: int | None
    blocklist_enabled: bool | None
    cache_size_mb: int | None
    config_dir: str | None
    default_trackers: Annotated[list[list[str]] | None, AfterValidator(validate_tiers)]
    download_dir: str | None
    download_queue_size: int | None
    download_queue_enabled: bool | None
    dht_enabled: bool | None
    encryption: str | None
    idle_seeding_limit: int | None
    idle_seeding_limit_enabled: bool | None
    incomplete_dir: str | None
    incomplete_dir_enabled: bool | None
    lpd_enabled: bool | None
    peer_limit_global: int | None
    peer_limit_per_torrent: int | None
    pex_enabled: bool | None
    peer_port: int | None
    peer_port_random_on_start: bool | None
    port_forwarding_enabled: bool | None
    queue_stalled_enabled: bool | None
    queue_stalled_minutes: int | None
    rename_partial_files: bool | None
    reqq: int | None
    rpc_version: int | None
    rpc_version_minimum: int | None
    rpc_version_semver: str | None
    script_torrent_added_enabled: bool | None
    script_torrent_added_filename: str | None
    script_torrent_done_seeding_enabled: bool | None
    script_torrent_done_seeding_filename: str | None
    script_torrent_done_filename: str | None
    script_torrent_done_enabled: bool | None
    seed_ratio_limit: float | None
    seed_ratio_limited: bool | None
    seed_queue_size: int | None
    seed_queue_enabled: bool | None
    session_id: str | None
    speed_limit_down: int | None
    speed_limit_down_enabled: bool | None
    speed_limit_up: int | None
    speed_limit_up_enabled: bool | None
    start_added_torrents: bool | None
    trash_original_torrent_files: bool | None
    units: Units | None
    utp_enabled: bool | None
    version: str | None
