from __future__ import annotations

from typing import Callable, Sequence

from flamiche.types import Receive, Scope, Send

__all__ = ("Router",)


class Route:
    def __init__(self, path: str, methods: Sequence[str]):
        self.path = path
        self.methods = methods

    def handles_method(self, method: str) -> bool:
        raise NotImplementedError


class Router:
    """
    Represents an ASGI callable that routes the given
    scope to the appropriate route handler.

    :param prefix: The URL prefix for the router.
        The prefix is prepended to every route added
        on the :class:`Router` instance.

    :param case_sensitive: Whether case sensitive
        URL matching is enabled.

    :param strict: Whether strict routing is enabled. When
        disabled, URLs with trailing slashes are ignored.
    """

    route_class = Route

    def __init__(
        self,
        *,
        prefix: str = "",
        case_sensitive: bool = False,
        strict: bool = False,
    ):
        self.prefix = prefix
        self.case_sensitive = case_sensitive
        self.strict = strict
        self.middleware = []
        self.routes = []

    def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        raise NotImplementedError

    def exception_handler(self):
        raise NotImplementedError

    def reset(self) -> Router:
        raise NotImplementedError

    def add_router(self, router: Router, *, prefix: str = "") -> Router:
        raise NotImplementedError

    def add_route(
        self,
        path: str,
        methods: Sequence[str],
        name: str | None = None,
    ) -> Callable:
        raise NotImplementedError

    def get(self, path: str, name: str | None = None) -> Callable:
        return self.add_route(path=path, name=name, methods=["GET"])

    def post(self, path: str, name: str | None = None) -> Callable:
        return self.add_route(path=path, name=name, methods=["POST"])

    def patch(self, path: str, name: str | None = None) -> Callable:
        return self.add_route(path=path, name=name, methods=["PATCH"])

    def put(self, path: str, name: str | None = None) -> Callable:
        return self.add_route(path=path, name=name, methods=["PUT"])

    def delete(self, path: str, name: str | None = None) -> Callable:
        return self.add_route(path=path, name=name, methods=["DELETE"])

    def options(self, path: str, name: str | None = None) -> Callable:
        return self.add_route(path=path, name=name, methods=["OPTIONS"])

    def head(self, path: str, name: str | None = None) -> Callable:
        return self.add_route(path=path, name=name, methods=["HEAD"])

    def trace(self, path: str, name: str | None = None) -> Callable:
        return self.add_route(path=path, name=name, methods=["TRACE"])
