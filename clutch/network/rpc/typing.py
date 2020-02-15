from typing import Union, Literal, Sequence, NamedTuple

IdsArg = Union[int, Sequence[Union[str, int]], Literal["recently_active"]]


class TrackerReplace(NamedTuple):
    trackerId: int
    announceUrl: str


FlatTrackerReplaceArg = Sequence[Union[int, str]]
