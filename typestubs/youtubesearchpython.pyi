from typing import Any, Dict

class VideosSearch:
    def __init__(
        self, query: str, limit: int = ..., language: str = ..., region: str = ...
    ) -> None: ...
    def result(self, mode: int = ...) -> Dict[str, Any]: ...