from clutch.method.misc import MiscellaneousMethods
from clutch.method.queue import QueueMethods
from clutch.method.session import SessionMethods
from clutch.method.torrent import TorrentMethods
from clutch.network.connection import Connection
from clutch.network.session import TransmissionSession
from clutch.network.utility import make_endpoint


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
        debug=False,
    ):
        self._endpoint: str = make_endpoint(address, scheme, host, port, path, query)
        self._session: TransmissionSession = TransmissionSession(username, password)
        self._connection: Connection = Connection(self._endpoint, self._session, debug)

    def set_rpc_debug(self, value: bool):
        self._connection.debug = value

    def set_connection(
        self,
        address="http://localhost:9091/transmission/rpc",
        scheme=None,
        host=None,
        port=None,
        path=None,
        query=None,
        username=None,
        password=None,
        debug=False,
    ):
        self._endpoint = make_endpoint(address, scheme, host, port, path, query)
        self._session = TransmissionSession(username, password)
        self._connection = Connection(self._endpoint, self._session, debug)
