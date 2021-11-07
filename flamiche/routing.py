from __future__ import annotations

from typing import Any, Callable

__all__ = ("Router",)


class Route:
    def __init__(self, path: str):
        self.path = path

    def handles_method(self, method: str) -> bool:
        pass


class Router:
    route_class = Route
    middleware: list[Callable[..., Any]]

    def __init__(
        self,
        prefix: str = "",
        case_sensitive: bool = False,
        strict: bool = False,
    ):
        self.prefix = prefix
        self.case_sensitive = case_sensitive
        self.strict = strict
        self.middleware = []

    def __call__(self, path: str, method: str):
        pass

    def use(self, middleware: Callable[..., Any]) -> Router:
        self.middleware.append(middleware)
        return self

    def route(self, path: str, method: str, handler: Callable[..., Any]):
        pass

    def reset(self) -> Router:
        pass

    def add_router(self, router: Router) -> Router:
        pass
