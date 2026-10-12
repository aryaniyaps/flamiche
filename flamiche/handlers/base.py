class BaseHandler:
    """Base request handler."""

    request_class = None

    def get_response(self, request) -> None:
        pass
