from typing import Dict, List


class Layer:
    strict: bool
    sensitive: bool

    def __init__(self, path: str, sensitive: bool, strict: bool, callback):
        self._path = path
        self.handle = callback
        self.params = None
        self.path = None
        self.regexp = None
        self.sensitive = sensitive
        self.strict = strict

    def handle_error(self, error, req, res, call_next) -> None:
        pass

    def handle_request(self, req, res, call_next) -> None:
        pass

    def match(self, path) -> bool:
        pass


class Route:
    stack: List[Layer]
    methods: Dict[str, bool]

    def __init__(self, path: str):
        self.path = path
        self.methods = {}
        self.stack = []

    def handles_method(self, method: str) -> bool:
        # check whether the route can handle this method.
        pass

    def options(self) -> List[str]:
        # supported HTTP methods
        methods = list(self.methods.keys())
        if self.methods.get("get", None) and not self.methods.get("head", None):
            methods.append("head")

        i = 0
        for _ in methods:
            methods[i] = methods[i].upper()
            i += 1
        return methods

    def dispatch(self, req, res, done):
        # dispatches the given route.
        pass


class Router:
    strict: bool
    case_sensitive: bool
    stack: List[Layer]

    def __init__(self, case_sensitive: bool, strict: bool):
        self.params = {}
        self._params = []
        self.case_sensitive = case_sensitive
        self.strict = strict
