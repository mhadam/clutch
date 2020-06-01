from typing import TypeVar

from pydantic import BaseModel

from clutch.compat import Type
from clutch.network.rpc.message import Response, Request
from clutch.network.session import TransmissionSession

T = TypeVar("T", bound=BaseModel)


class Connection:
    def __init__(
        self, endpoint: str, session: TransmissionSession, debug: bool = False
    ):
        self.endpoint = endpoint
        self.session = session
        self.debug = debug

    def send(self, request: Request, model: Type[T] = None) -> Response[T]:
        data = request.json(by_alias=True, exclude_none=True).encode("utf-8")
        if self.debug:
            print(f"RPC request sent to {self.endpoint}:")
            print(data)
        response = self.session.post(self.endpoint, data=data)
        if model is not None:
            if self.debug:
                print("RPC response received:")
                print(response.text)
            return Response[model].parse_raw(response.text)  # type: ignore
        else:
            return Response.parse_raw(response.text)
