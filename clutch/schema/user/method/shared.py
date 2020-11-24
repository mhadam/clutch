from typing import Union, Set

from clutch.compat import Literal

TorrentId = Union[int, str]

IdsArg = Union[int, Set[TorrentId], Literal["recently_active"]]
