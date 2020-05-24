from urllib.parse import urlparse

from requests import Session
from requests.auth import HTTPBasicAuth


class TransmissionAuth(HTTPBasicAuth):
    HEADER_NAME = "X-Transmission-Session-Id"
    HEADER_NAME_LOWER = HEADER_NAME.lower()

    def __init__(self, username=None, password=None):
        # setup any auth-related data here
        self.__csrf_tokens = {}
        super(TransmissionAuth, self).__init__(username, password)

    def handle_409(self, r, **kwargs):
        """handles CSRF token expiration and resends the request"""

        # cannot handle the request
        if self.HEADER_NAME not in r.headers:
            return

        url = r.url
        self.__csrf_tokens[url] = r.headers[self.HEADER_NAME]

        # copy the original headers
        new_headers = dict(
            (k, v)
            for k, v in r.request.headers.items()
            if k.lower()
            not in ("content-length", "content-type", self.HEADER_NAME_LOWER)
        )

        new_headers["Host"] = urlparse(r.request.url).netloc
        new_request = r.request.copy()
        new_request.headers.update(new_headers)
        new_request.headers[self.HEADER_NAME] = self.__csrf_tokens[url]

        r.close()
        _r = r.connection.send(new_request, **kwargs)
        _r.history.append(r)
        _r.request = new_request
        return _r

    def __call__(self, r):
        """adds the appropriate CSRF token to the headers"""
        # don't use authentication if username and password aren't defined
        if self.username is not None and self.password is not None:
            r = super(TransmissionAuth, self).__call__(r)

        token = self.__csrf_tokens.get(r.url)
        if token:
            r.headers[self.HEADER_NAME] = token
        r.register_hook("response", self.handle_409)
        return r


class TransmissionSession(Session):
    """
    Handles Transmission CSRF Protection
    https://trac.transmissionbt.com/browser/trunk/extras/rpc-spec.txt#L48
    """

    def __init__(self, username, password):
        super(TransmissionSession, self).__init__()
        self.auth = TransmissionAuth(username, password)
