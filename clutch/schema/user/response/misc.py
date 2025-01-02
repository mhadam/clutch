from pydantic import BaseModel

from clutch.schema.user.method.misc import IpProtocol


class BlocklistResponse(BaseModel):
    blocklist_size: int


class PortTestResponse(BaseModel):
    port_is_open: int
    ip_protocol: IpProtocol | None = None


class FreeSpaceResponse(BaseModel):
    path: str
    size_bytes: int
    total_size: int


class BandwidthGroup(BaseModel):
    honors_session_limits: bool
    name: str
    speed_limit_down_enabled: bool
    speed_limit_down: int
    speed_limit_up_enabled: bool
    speed_limit_up: int


class BandwidthGroupResponse(BaseModel):
    group: list[BandwidthGroup]
