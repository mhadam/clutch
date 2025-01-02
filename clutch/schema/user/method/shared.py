from typing import Literal, Union, Iterable

TorrentId = Union[int, str]

IdsArg = Union[
    int, Iterable[TorrentId], Iterable[int], Iterable[str], Literal["recently_active"]
]
