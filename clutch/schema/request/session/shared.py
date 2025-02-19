from typing import Literal, Tuple

from pydantic import BaseModel, Field

DataRateUnits = Tuple[
    Literal["KB/s"], Literal["MB/s"], Literal["GB/s"], Literal["TB/s"]
]
DataSizeUnits = Tuple[Literal["KB"], Literal["MB"], Literal["GB"], Literal["TB"]]
ByteDefinition = Literal[1000, 1024]


class UnitsRequest(BaseModel):
    speed_units: DataRateUnits = Field(..., serialization_alias="speed-units")
    speed_bytes: ByteDefinition = Field(..., serialization_alias="speed-bytes")
    size_units: DataSizeUnits = Field(..., serialization_alias="size-units")
    size_bytes: ByteDefinition = Field(..., serialization_alias="size-bytes")
    memory_units: DataSizeUnits = Field(..., serialization_alias="memory-units")
    memory_bytes: ByteDefinition = Field(..., serialization_alias="memory-bytes")
