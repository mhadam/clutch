from typing import Self, Sequence

from pydantic import BaseModel, Field, model_validator


class Cookie(BaseModel):
    name: str
    content: str


class TorrentAddArgumentsRequest(BaseModel):
    cookies: Sequence[Cookie] | None = None
    download_dir: str | None = Field(None, serialization_alias="download-dir")
    filename: str | None = None
    metainfo: str | None = None
    paused: bool | None = None
    peer_limit: int | None = Field(None, serialization_alias="peer-limit")
    bandwidth_priority: int | None = Field(
        None, serialization_alias="bandwidthPriority"
    )
    files_wanted: Sequence[int] | None = Field(
        None, serialization_alias="files-wanted"
    )
    files_unwanted: Sequence[int] | None = Field(
        None, serialization_alias="files-unwanted"
    )
    priority_high: Sequence[int] | None = Field(
        None, serialization_alias="priority-high"
    )
    priority_low: Sequence[int] | None = Field(
        None, serialization_alias="priority-low"
    )
    priority_normal: Sequence[int] | None = Field(
        None, serialization_alias="priority-normal"
    )

    @model_validator(mode="after")
    def check_required_exclusive_fields(self) -> Self:
        if self.filename is not None and self.metainfo is not None:
            raise ValueError("Both filename and metainfo fields are in request")
        if self.filename is None and self.metainfo is None:
            raise ValueError("Either filename or metainfo field is required in request")
        return self
