from typing import Sequence, Optional

from pydantic import BaseModel, Field, root_validator


class Cookie(BaseModel):
    name: str
    content: str


class TorrentAddArgumentsRequest(BaseModel):
    cookies: Optional[Sequence[Cookie]]
    download_dir: Optional[str] = Field(None, alias="download-dir")
    filename: Optional[str] = None
    metainfo: Optional[str] = None
    paused: Optional[bool] = None
    peer_limit: Optional[int] = Field(None, alias="peer-limit")
    bandwidth_priority: Optional[int] = Field(None, alias="bandwidthPriority")
    files_wanted: Optional[Sequence[int]] = Field(None, alias="files-wanted")
    files_unwanted: Optional[Sequence[int]] = Field(None, alias="files-unwanted")
    priority_high: Optional[Sequence[int]] = Field(None, alias="priority-high")
    priority_low: Optional[Sequence[int]] = Field(None, alias="priority-low")
    priority_normal: Optional[Sequence[int]] = Field(None, alias="priority-normal")

    class Config:
        allow_population_by_field_name = True

    @root_validator
    def check_required_exclusive_fields(cls, values):
        filename, metainfo = (
            values.get("filename"),
            values.get("metainfo"),
        )
        if filename is not None and metainfo is not None:
            raise ValueError("Both filename and metainfo fields are in request")
        if filename is None and metainfo is None:
            raise ValueError("Either filename or metainfo field is required in request")
        return values
