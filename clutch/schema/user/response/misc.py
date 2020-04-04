from pydantic import BaseModel


class BlocklistResponse(BaseModel):
    blocklist_size: int


class PortTestResponse(BaseModel):
    port_is_open: int


class FreeSpaceResponse(BaseModel):
    path: str
    size_bytes: int
