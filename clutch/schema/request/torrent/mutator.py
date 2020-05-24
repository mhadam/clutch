from typing import Sequence, Optional

from pydantic import BaseModel, Field

from clutch.schema.user.method.shared import IdsArg


class TrackerReplaceRequest(BaseModel):
    tracker_id: int = Field(None, alias="trackerId")
    announce_url: str = Field(None, alias="announceUrl")

    class Config:
        allow_population_by_field_name = True


class TorrentMutatorArgumentsRequest(BaseModel):
    bandwidth_priority: Optional[int] = Field(None, alias="bandwidthPriority")
    download_limit: Optional[int] = Field(None, alias="downloadLimit")
    download_limited: Optional[bool] = Field(None, alias="downloadLimited")
    edit_date: Optional[int] = Field(None, alias="editDate")
    files_wanted: Optional[Sequence[str]] = Field(None, alias="files-wanted")
    files_unwanted: Optional[Sequence[str]] = Field(None, alias="file-unwanted")
    honors_session_limits: Optional[bool] = Field(None, alias="honors-session-limits")
    ids: Optional[IdsArg]
    labels: Optional[Sequence[str]]
    location: Optional[str]
    peer_limit: Optional[int] = Field(None, alias="peer-limit")
    priority_high: Optional[Sequence[str]] = Field(None, alias="priority-high")
    priority_low: Optional[Sequence[str]] = Field(None, alias="priority-low")
    priority_normal: Optional[Sequence[str]] = Field(None, alias="priority-normal")
    queue_position: Optional[int] = Field(None, alias="queuePosition")
    seed_idle_limit: Optional[int] = Field(None, alias="seedIdleLimit")
    seed_idle_mode: Optional[int] = Field(None, alias="seedIdleMode")
    seed_ratio_limit: Optional[float] = Field(None, alias="seedRatioLimit")
    seed_ratio_mode: Optional[int] = Field(None, alias="seedRatioMode")
    tracker_add: Optional[Sequence[str]] = Field(None, alias="trackerAdd")
    tracker_remove: Optional[Sequence[str]] = Field(None, alias="trackerRemove")
    tracker_replace: Optional[Sequence[TrackerReplaceRequest]] = Field(
        None, alias="trackerReplace"
    )
    upload_limit: Optional[int] = Field(None, alias="uploadLimit")
    upload_limited: Optional[bool] = Field(None, alias="uploadLimited")

    class Config:
        allow_population_by_field_name = True
