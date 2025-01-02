from typing import Sequence

from pydantic import BaseModel, Field

from clutch.schema.user.method.shared import IdsArg


class TorrentMutatorArgumentsRequest(BaseModel):
    bandwidth_priority: int | None = Field(
        None, serialization_alias="bandwidthPriority"
    )
    download_limit: int | None = Field(None, serialization_alias="downloadLimit")
    download_limited: bool | None = Field(None, serialization_alias="downloadLimited")
    edit_date: int | None = Field(None, serialization_alias="editDate")
    files_wanted: Sequence[int] | None = Field(None, serialization_alias="files-wanted")
    files_unwanted: Sequence[int] | None = Field(
        None, serialization_alias="files-unwanted"
    )
    group: str | None = Field(None)
    honors_session_limits: bool | None = Field(
        None, serialization_alias="honorsSessionLimits"
    )
    ids: IdsArg | None = None
    labels: Sequence[str] | None = None
    location: str | None = None
    peer_limit: int | None = Field(None, serialization_alias="peer-limit")
    priority_high: Sequence[int] | None = Field(
        None, serialization_alias="priority-high"
    )
    priority_low: Sequence[int] | None = Field(None, serialization_alias="priority-low")
    priority_normal: Sequence[int] | None = Field(
        None, serialization_alias="priority-normal"
    )
    queue_position: int | None = Field(None, serialization_alias="queuePosition")
    seed_idle_limit: int | None = Field(None, serialization_alias="seedIdleLimit")
    seed_idle_mode: int | None = Field(None, serialization_alias="seedIdleMode")
    seed_ratio_limit: float | None = Field(None, serialization_alias="seedRatioLimit")
    seed_ratio_mode: int | None = Field(None, serialization_alias="seedRatioMode")
    tracker_list: str | None = Field(None, serialization_alias="trackerList")
    upload_limit: int | None = Field(None, serialization_alias="uploadLimit")
    upload_limited: bool | None = Field(None, serialization_alias="uploadLimited")
