
from pydantic import BaseModel


class BandwidthGroupArgumentsRequest(BaseModel):
    group: str | list[str] | None = None
