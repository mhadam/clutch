from typing import TypeVar

from pydantic import BaseModel

from clutch.compat import Type
from clutch.network.rpc.message import Response, Request
from clutch.network.session import TransmissionSession

T = TypeVar("T", bound=BaseModel)


class Connection:
    def __init__(self, endpoint: str, session: TransmissionSession):
        self.endpoint = endpoint
        self.session = session

    def send(self, request: Request, model: Type[T] = None) -> Response[T]:
        response = self.session.post(
            self.endpoint,
            data=request.json(by_alias=True, exclude_none=True).encode("utf-8"),
        )
        if model is not None:
            return Response[model].parse_raw(response.text)  # type: ignore
        else:
            return Response.parse_raw(response.text)
