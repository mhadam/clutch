from typing import Type, TypeVar

from pydantic import BaseModel

from clutch.network.rpc.message import Request, Response
from clutch.network.session import TransmissionSession

T = TypeVar("T", bound=BaseModel)


class Connection:
    def __init__(
        self, endpoint: str, session: TransmissionSession, debug: bool = False
    ):
        self.endpoint = endpoint
        self.session = session
        self.debug = debug

    def send(self, request: Request, model: Type[T] | None = None) -> Response[T]:
        data = request.model_dump_json(by_alias=True, exclude_none=True).encode("utf-8")
        response = self.session.post(self.endpoint, data=data)
        if model is not None:
            return Response[model].model_validate_json(response.text)  # type: ignore
        else:
            return Response.model_validate_json(response.text)
