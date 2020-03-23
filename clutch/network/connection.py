import json
from json import JSONDecodeError
from typing import Optional, Any, Mapping

from clutch.network.encoding import TransmissionJSONEncoder
from clutch.network.rpc.message import Response, Request
from clutch.network.session import TransmissionSession


def _encode_request(rpc_request: Request) -> bytes:
    # encoding should be UTF-8
    # https://trac.transmissionbt.com/browser/trunk/extras/rpc-spec.txt#L19
    return json.dumps(
        rpc_request, ensure_ascii=False, cls=TransmissionJSONEncoder
    ).encode("utf-8")


def _convert_to_domain(response: Mapping[str, Any]) -> Response[Mapping[str, object]]:
    output = Response(result=response["result"])
    try:
        output.arguments = response["arguments"]
        output.tag = response["tag"]
    except KeyError:
        # TODO: log here possibly
        pass

    return output


def _validate_response(response: Mapping[str, Any]) -> bool:
    def validate_result() -> bool:
        return isinstance(response.get("result"), str)

    def validate_arguments() -> bool:
        value = response.get("arguments")
        return value is None or isinstance(value, dict)

    def validate_tag() -> bool:
        value = response.get("tag")
        return value is None or isinstance(value, int)

    return validate_result() and validate_arguments() and validate_tag()


class Connection:
    def __init__(self, endpoint: str, session: TransmissionSession):
        self.endpoint = endpoint
        self.session = session

    def send(self, request: Request) -> Optional[Response[Mapping[str, object]]]:
        response = self.session.post(self.endpoint, data=_encode_request(request))
        try:
            decoded_response = json.loads(response.text)
            if _validate_response(decoded_response):
                return _convert_to_domain(decoded_response)
        except JSONDecodeError as e:
            print(f"{response.text}")
            print(e)
        return None
