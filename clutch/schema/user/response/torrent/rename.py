from pydantic import BaseModel


class TorrentRename(BaseModel):
    path: str
    name: str
    id: int
