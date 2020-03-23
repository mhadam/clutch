from typing import TypedDict, Literal, Union, Sequence


class TorrentRenameArguments(TypedDict):
    ids: Sequence[Union[str, int]]
    path: str
    name: str


class TorrentRenameResponse(TypedDict):
    path: str
    name: str
    id: int
