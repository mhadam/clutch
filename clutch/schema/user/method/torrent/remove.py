from clutch.compat import TypedDict

from clutch.schema.user.method.shared import IdsArg


class TorrentRemoveArgumentsOptional(TypedDict, total=False):
    delete_local_data: bool


class TorrentRemoveArguments(TorrentRemoveArgumentsOptional):
    ids: IdsArg
