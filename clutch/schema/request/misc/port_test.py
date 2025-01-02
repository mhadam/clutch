from typing import Literal, Tuple

from pydantic import BaseModel, Field

IpProtocol = Tuple[Literal["ipv4"] | Literal["ipv6"]]


class PortTestArgumentsRequest(BaseModel):
    ip_protocol: IpProtocol | None = Field(None, serialization_alias="ipProtocol")
