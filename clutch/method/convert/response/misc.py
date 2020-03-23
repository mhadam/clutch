from typing import TypedDict


class BlocklistResponse(TypedDict):
    blocklist_size: int


class PortTestResponse(TypedDict):
    port_is_open: int


class FreeSpaceResponse(TypedDict):
    path: str
    size_bytes: int
