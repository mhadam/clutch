from urllib.parse import urlsplit, urlunsplit


def make_endpoint(
    address: str = "http://localhost:9091/transmission/rpc",
    scheme: str = None,
    host: str = None,
    port: int = None,
    path: str = None,
    query: str = None,
) -> str:
    # any explicit keyword arguments override the default address
    url_info = urlsplit(address)
    if scheme is None:
        scheme = url_info.scheme
    if host is None:
        host = url_info.hostname
    if port is None:
        port = url_info.port
    if path is None:
        path = url_info.path
    if query is None:
        query = url_info.query
    return urlunsplit((scheme, f"{host}:{port}", path, query, None))
