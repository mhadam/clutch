from typing import Optional

from pydantic import BaseModel, root_validator


class Torrent(BaseModel):
    id: int
    name: str
    hash_string: str


class TorrentAdd(BaseModel):
    torrent_added: Optional[Torrent]
    torrent_duplicate: Optional[Torrent]

    @root_validator
    def check_exclusive_fields(cls, values):
        added, duplicate = (
            values.get("torrent_added"),
            values.get("torrent_duplicate"),
        )
        if added is not None and duplicate is not None:
            raise ValueError("Both torrent added and duplicate fields in response")
        return values
