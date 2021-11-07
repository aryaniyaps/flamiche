from flamiche.routing import Router

__all__ = ("Flamiche",)


class Flamiche:
    def __init__(self, prefix: str = ""):
        self.router = Router(prefix=prefix)
