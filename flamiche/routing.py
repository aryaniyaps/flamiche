__all__ = ("Router",)


class Route:
    def __init__(self, path: str):
        self.path = path

    def handles_method(self, method: str) -> bool:
        # check whether the route can handle this method.
        pass


class RouteMatcher:
    pass


class Router:
    pass
