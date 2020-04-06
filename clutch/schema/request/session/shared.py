from typing import Tuple

from pydantic import BaseModel, Field

from clutch.compat import Literal

DataRateUnits = Tuple[
    Literal["KB/s"], Literal["MB/s"], Literal["GB/s"], Literal["TB/s"]
]
DataSizeUnits = Tuple[Literal["KB"], Literal["MB"], Literal["GB"], Literal["TB"]]
ByteDefinition = Literal[1000, 1024]


class UnitsRequest(BaseModel):
    speed_units: DataRateUnits = Field(..., alias="speed-units")
    speed_bytes: ByteDefinition = Field(..., alias="speed-bytes")
    size_units: DataSizeUnits = Field(..., alias="size-units")
    size_bytes: ByteDefinition = Field(..., alias="size-bytes")
    memory_units: DataSizeUnits = Field(..., alias="memory-units")
    memory_bytes: ByteDefinition = Field(..., alias="memory-bytes")
