from typing import Union, Sequence, NamedTuple


class TrackerReplace(NamedTuple):
    trackerId: int
    announceUrl: str


FlatTrackerReplaceArg = Sequence[Union[int, str]]
