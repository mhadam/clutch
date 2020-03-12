from dataclasses import dataclass
from typing import Union, Sequence


@dataclass
class TrackerReplace:
    trackerId: int
    announceUrl: str


FlatTrackerReplaceArg = Sequence[Union[int, str]]
