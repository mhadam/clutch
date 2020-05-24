from typing import Tuple

from clutch.compat import Literal, TypedDict

# Todo: change these values, match to response schema
DataRateUnits = Tuple[
    Literal["kB/s"], Literal["MB/s"], Literal["GB/s"], Literal["TB/s"]
]
DataSizeUnits = Tuple[Literal["kB"], Literal["MB"], Literal["GB"], Literal["TB"]]
ByteDefinition = Literal[1000, 1024]


class Units(TypedDict):
    speed_units: DataRateUnits
    speed_bytes: ByteDefinition
    size_units: DataSizeUnits
    size_bytes: ByteDefinition
    memory_units: DataSizeUnits
    memory_bytes: ByteDefinition
