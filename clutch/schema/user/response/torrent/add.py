from typing import Self

from pydantic import BaseModel, model_validator


class Torrent(BaseModel):
    id: int
    name: str
    hash_string: str


class TorrentAdd(BaseModel):
    torrent_added: Torrent | None = None
    torrent_duplicate: Torrent | None = None

    @model_validator(mode="after")
    def check_exclusive_fields(self) -> Self:
        if self.torrent_added is not None and self.torrent_duplicate is not None:
            raise ValueError("Both torrent added and duplicate fields in response")
        return self
