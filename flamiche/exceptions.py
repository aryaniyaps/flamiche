from typing import Any, Dict, Optional

__all__ = ("HTTPException",)


class HTTPException(Exception):
    def __init__(
        self,
        status_code: int,
        detail: Optional[str] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.status_code = status_code
        self.detail = detail
