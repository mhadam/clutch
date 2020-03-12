from enum import Enum, unique
from typing import Optional

from clutch.method.method import MethodNamespace
from clutch.method.shared import construct_request
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
    ) -> Optional[Response]:
        request = construct_request(
            method=movement.value, arguments={"ids": ids}, tag=tag
        )
        return self._connection.send(request)
