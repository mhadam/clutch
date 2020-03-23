from enum import Enum, unique
from typing import Optional, Mapping

from mypy.types import NoneType

from clutch.method.group.method import MethodNamespace
from clutch.method.group.shared import construct_request
from clutch.method.typing.torrent.action import IdsArg
from clutch.network.rpc.message import Response


@unique
class QueueMovement(Enum):
    TOP = "queue-move-top"
    UP = "queue-move-up"
    DOWN = "queue-move-down"
    BOTTOM = "queue-move-bottom"


class QueueMethods(MethodNamespace):
    def move(
        self, movement: QueueMovement, ids: IdsArg, tag: int = None
    ) -> Response[Mapping[str, object]]:
        """Change the position of one or more torrents in the queue."""
        request = construct_request(
            method=movement.value, arguments={"ids": ids}, tag=tag
        )
        return self._connection.send(request)
