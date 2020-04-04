from typing import Optional

from pydantic import BaseModel, Field, root_validator

from clutch.schema.request.session.shared import UnitsRequest


class SessionMutatorArgumentsRequest(BaseModel):
    alt_speed_down: Optional[int] = Field(None, alias="alt-speed-down")
    alt_speed_enabled: Optional[bool] = Field(None, alias="alt-speed-enabled")
    alt_speed_time_begin: Optional[int] = Field(None, alias="alt-speed-time-begin")
    alt_speed_time_enabled: Optional[bool] = Field(None, alias="alt-speed-time-enabled")
    alt_speed_time_end: Optional[int] = Field(None, alias="alt-speed-time-end")
    alt_speed_time_day: Optional[int] = Field(None, alias="alt-speed-time-day")
    alt_speed_up: Optional[int] = Field(None, alias="alt-speed-up")
    blocklist_url: Optional[str] = Field(None, alias="blocklist-url")
    blocklist_enabled: Optional[bool] = Field(None, alias="blocklist-enabled")
    cache_size_mb: Optional[int] = Field(None, alias="cache-size-mb")
    download_dir: Optional[str] = Field(None, alias="download-dir")
    download_queue_size: Optional[int] = Field(None, alias="download-queue-size")
    download_queue_enabled: Optional[bool] = Field(None, alias="download-queue-enabled")
    dht_enabled: Optional[bool] = Field(None, alias="dht-enabled")
    encryption: Optional[str] = None
    idle_seeding_limit: Optional[int] = Field(None, alias="idle-seeding-limit")
    idle_seeding_limit_enabled: Optional[bool] = Field(
        None, alias="idle-seeding-limit-enabled"
    )
    incomplete_dir: Optional[str] = Field(None, alias="incomplete-dir")
    incomplete_dir_enabled: Optional[bool] = Field(None, alias="incomplete-dir-enabled")
    lpd_enabled: Optional[bool] = Field(None, alias="lpd-enabled")
    peer_limit_global: Optional[int] = Field(None, alias="peer-limit-global")
    peer_limit_per_torrent: Optional[int] = Field(None, alias="peer-limit-per-torrent")
    pex_enabled: Optional[bool] = Field(None, alias="pex-enabled")
    peer_port: Optional[int] = Field(None, alias="peer-port")
    peer_port_random_on_start: Optional[bool] = Field(
        None, alias="peer-port-random-on-start"
    )
    port_forwarding_enabled: Optional[bool] = Field(
        None, alias="port-forwarding-enabled"
    )
    queue_stalled_enabled: Optional[bool] = Field(None, alias="queue-stalled-enabled")
    queue_stalled_minutes: Optional[int] = Field(None, alias="queue-stalled-minutes")
    rename_partial_files: Optional[bool] = Field(None, alias="rename-partial-files")
    script_torrent_done_filename: Optional[str] = Field(
        None, alias="script-torrent-done-filename"
    )
    script_torrent_done_enabled: Optional[bool] = Field(
        None, alias="script-torrent-done-enabled"
    )
    seed_ratio_limit: Optional[float] = Field(None, alias="seedRatioLimit")
    seed_ratio_limited: Optional[bool] = Field(None, alias="seedRatioLimited")
    seed_queue_size: Optional[int] = Field(None, alias="seed-queue-size")
    seed_queue_enabled: Optional[bool] = Field(None, alias="seed-queue-enabled")
    speed_limit_down: Optional[int] = Field(None, alias="speed-limit-down")
    speed_limit_down_enabled: Optional[bool] = Field(
        None, alias="speed-limit-down-enabled"
    )
    speed_limit_up: Optional[int] = Field(None, alias="speed-limit-up")
    speed_limit_up_enabled: Optional[bool] = Field(None, alias="speed-limit-up-enabled")
    start_added_torrents: Optional[bool] = Field(None, alias="start-added-torrents")
    trash_original_torrent_files: Optional[bool] = Field(
        None, alias="trash-original-torrent-files"
    )
    units: Optional[UnitsRequest] = None
    utp_enabled: Optional[bool] = Field(None, alias="utp-enabled")

    class Config:
        allow_population_by_field_name = True

    @root_validator
    def at_least_one_field(cls, values):
        if len(values) < 1:
            raise ValueError("At least one valid argument must be supplied")
        return values
