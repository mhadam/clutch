from typing import Annotated, Any, Generic, TypeVar

from pydantic import BaseModel, FieldSerializationInfo, PlainSerializer, field_validator

from clutch.network.rpc.convert import normalize_arguments

T = TypeVar("T")


def dict_not_none_ser(
    value: dict[str, Any], info: FieldSerializationInfo
) -> dict[str, Any]:
    if isinstance(value, dict) and info.exclude_none:
        return {k: v for k, v in value.items() if v is not None}
    else:
        return value


class Request(BaseModel, Generic[T]):
    """RPC request container"""

    method: str
    arguments: Annotated[T | None, PlainSerializer(dict_not_none_ser)] = None
    tag: int | None = None


class Response(BaseModel, Generic[T]):
    """RPC response container"""

    result: str
    arguments: T | None = None
    tag: int | None = None

    @field_validator("arguments", mode="before")
    @classmethod
    def fields_underscored(cls, v: Any):
        if isinstance(v, dict):
            return normalize_arguments(v)
        else:
            return v
