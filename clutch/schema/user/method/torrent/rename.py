from typing import Sequence, TypedDict, Union


class TorrentRenameArguments(TypedDict):
    ids: Sequence[Union[str, int]]
    path: str
    name: str
