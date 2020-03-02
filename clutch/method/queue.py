from enum import Enum, unique

from typing import Optional

from clutch.method.method import MethodNamespace
from clutch.network.rpc.message import Response, Request
from clutch.network.rpc.torrent.action import IdsArg


@unique
class QueueMovement(Enum):
    TOP = "queue-move-top"
    UP = "queue-move-up"
    DOWN = "queue-move-down"
    BOTTOM = "queue-move-bottom"


class QueueMethods(MethodNamespace):
    def move(
            self,
            movement: QueueMovement,
            ids: IdsArg,
            tag: int = None
    ) -> Optional[Response]:
        request = Request(method=movement.value)
        request["arguments"] = {'ids': ids}
        if tag is not None:
            request["tag"] = tag
        return self._connection.send(request)
