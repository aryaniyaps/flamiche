from http.client import HTTPConnection


class TestClient:
    def __init__(self) -> None:
        self.connection = HTTPConnection()
