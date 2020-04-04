from enum import Enum, unique

from clutch.method.method import MethodNamespace
from clutch.network.rpc.message import Response, Request
from clutch.schema.user.method.shared import IdsArg


@unique
class QueueMovement(Enum):
    TOP = "queue-move-top"
    UP = "queue-move-up"
    DOWN = "queue-move-down"
    BOTTOM = "queue-move-bottom"


class QueueMethods(MethodNamespace):
    def move(self, movement: QueueMovement, ids: IdsArg, tag: int = None) -> Response:
        """Change the position of one or more torrents in the queue."""
        return self._connection.send(
            Request(method=movement.value, arguments={"ids": ids}, tag=tag)
        )
