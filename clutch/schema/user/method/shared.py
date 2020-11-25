from typing import Union, Set

from clutch.compat import Literal

TorrentId = Union[int, str]

IdsArg = Union[int, Set[TorrentId], Set[int], Set[str], Literal["recently_active"]]
