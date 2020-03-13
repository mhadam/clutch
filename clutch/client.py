from clutch.method.group.queue import QueueMethods
from clutch.method.group.session import SessionMethods
from clutch.method.group.torrent import TorrentMethods
from clutch.network.connection import Connection
from clutch.network.session import TransmissionSession
from clutch.network.utility import make_endpoint
from clutch.method.group.misc import MiscellaneousMethods


class Client:

    session: SessionMethods = SessionMethods()
    torrent: TorrentMethods = TorrentMethods()
    queue: QueueMethods = QueueMethods()
    misc: MiscellaneousMethods = MiscellaneousMethods()

    def __init__(
        self,
        address="http://localhost:9091/transmission/rpc",
        scheme=None,
        host=None,
        port=None,
        path=None,
        query=None,
        username=None,
        password=None,
        timeout=None,
    ):
        self._rpc_version = None
        self._timeout = timeout
        self._endpoint: str = make_endpoint(address, scheme, host, port, path, query)
        self._session: TransmissionSession = TransmissionSession(username, password)
        self._connection: Connection = Connection(self._endpoint, self._session)
