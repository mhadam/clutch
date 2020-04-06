from typing import Union, Sequence

from clutch.compat import TypedDict


class TorrentRenameArguments(TypedDict):
    ids: Sequence[Union[str, int]]
    path: str
    name: str
