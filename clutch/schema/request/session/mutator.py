from typing import Self

from pydantic import BaseModel, Field, model_validator

from clutch.schema.request.session.shared import UnitsRequest


class SessionMutatorArgumentsRequest(BaseModel):
    alt_speed_down: int | None = Field(None, serialization_alias="alt-speed-down")
    alt_speed_enabled: bool | None = Field(
        None, serialization_alias="alt-speed-enabled"
    )
    alt_speed_time_begin: int | None = Field(
        None, serialization_alias="alt-speed-time-begin"
    )
    alt_speed_time_enabled: bool | None = Field(
        None, serialization_alias="alt-speed-time-enabled"
    )
    alt_speed_time_end: int | None = Field(
        None, serialization_alias="alt-speed-time-end"
    )
    alt_speed_time_day: int | None = Field(
        None, serialization_alias="alt-speed-time-day"
    )
    alt_speed_up: int | None = Field(None, serialization_alias="alt-speed-up")
    blocklist_url: str | None = Field(None, serialization_alias="blocklist-url")
    blocklist_enabled: bool | None = Field(
        None, serialization_alias="blocklist-enabled"
    )
    cache_size_mb: int | None = Field(None, serialization_alias="cache-size-mb")
    download_dir: str | None = Field(None, serialization_alias="download-dir")
    download_queue_size: int | None = Field(
        None, serialization_alias="download-queue-size"
    )
    download_queue_enabled: bool | None = Field(
        None, serialization_alias="download-queue-enabled"
    )
    dht_enabled: bool | None = Field(None, serialization_alias="dht-enabled")
    encryption: str | None = None
    idle_seeding_limit: int | None = Field(
        None, serialization_alias="idle-seeding-limit"
    )
    idle_seeding_limit_enabled: bool | None = Field(
        None, serialization_alias="idle-seeding-limit-enabled"
    )
    incomplete_dir: str | None = Field(None, serialization_alias="incomplete-dir")
    incomplete_dir_enabled: bool | None = Field(
        None, serialization_alias="incomplete-dir-enabled"
    )
    lpd_enabled: bool | None = Field(None, serialization_alias="lpd-enabled")
    peer_limit_global: int | None = Field(
        None, serialization_alias="peer-limit-global"
    )
    peer_limit_per_torrent: int | None = Field(
        None, serialization_alias="peer-limit-per-torrent"
    )
    pex_enabled: bool | None = Field(None, serialization_alias="pex-enabled")
    peer_port: int | None = Field(None, serialization_alias="peer-port")
    peer_port_random_on_start: bool | None = Field(
        None, serialization_alias="peer-port-random-on-start"
    )
    port_forwarding_enabled: bool | None = Field(
        None, serialization_alias="port-forwarding-enabled"
    )
    queue_stalled_enabled: bool | None = Field(
        None, serialization_alias="queue-stalled-enabled"
    )
    queue_stalled_minutes: int | None = Field(
        None, serialization_alias="queue-stalled-minutes"
    )
    rename_partial_files: bool | None = Field(
        None, serialization_alias="rename-partial-files"
    )
    script_torrent_done_filename: str | None = Field(
        None, serialization_alias="script-torrent-done-filename"
    )
    script_torrent_done_enabled: bool | None = Field(
        None, serialization_alias="script-torrent-done-enabled"
    )
    seed_ratio_limit: float | None = Field(
        None, serialization_alias="seedRatioLimit"
    )
    seed_ratio_limited: bool | None = Field(
        None, serialization_alias="seedRatioLimited"
    )
    seed_queue_size: int | None = Field(None, serialization_alias="seed-queue-size")
    seed_queue_enabled: bool | None = Field(
        None, serialization_alias="seed-queue-enabled"
    )
    speed_limit_down: int | None = Field(
        None, serialization_alias="speed-limit-down"
    )
    speed_limit_down_enabled: bool | None = Field(
        None, serialization_alias="speed-limit-down-enabled"
    )
    speed_limit_up: int | None = Field(None, serialization_alias="speed-limit-up")
    speed_limit_up_enabled: bool | None = Field(
        None, serialization_alias="speed-limit-up-enabled"
    )
    start_added_torrents: bool | None = Field(
        None, serialization_alias="start-added-torrents"
    )
    trash_original_torrent_files: bool | None = Field(
        None, serialization_alias="trash-original-torrent-files"
    )
    units: UnitsRequest | None = None
    utp_enabled: bool | None = Field(None, serialization_alias="utp-enabled")

    @model_validator(mode="after")
    def at_least_one_field(self) -> Self:
        dumped = self.model_dump()
        if len(dumped) < 1:
            raise ValueError("At least one valid argument must be supplied")
        return self
