from typing import TypedDict, Literal, Tuple
from clutch.network.rpc.session.shared import SessionArguments


class SessionAccessorOptional(TypedDict, total=False):
    tag: int
    arguments: SessionArguments


class SessionAccessor(SessionAccessorOptional):
    method: Literal["session-get"]
