from typing import TypedDict, Literal

from clutch.method.typing.session.shared import SessionArguments


class SessionAccessorOptional(TypedDict, total=False):
    tag: int
    arguments: SessionArguments


class SessionAccessor(SessionAccessorOptional):
    method: Literal["session-get"]
