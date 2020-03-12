from typing import TypedDict, Literal

from clutch.method.typing.session.shared import SessionArguments

SessionAccessorArguments = SessionArguments


class SessionAccessorOptional(TypedDict, total=False):
    tag: int
    arguments: SessionAccessorArguments


class SessionAccessor(SessionAccessorOptional):
    method: Literal["session-get"]
