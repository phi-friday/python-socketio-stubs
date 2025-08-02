from typing import Any

import engineio
from socketio.base_server import BaseServer

class WSGIApp(engineio.WSGIApp):
    def __init__(
        self,
        socketio_app: BaseServer[Any, Any],
        wsgi_app: Any = ...,
        static_files: dict[str, dict[str, str]] | None = ...,
        socketio_path: str = ...,
    ) -> None: ...

class Middleware(WSGIApp):
    def __init__(
        self,
        socketio_app: BaseServer[Any, Any],
        wsgi_app: Any = ...,
        socketio_path: str = ...,
    ) -> None: ...
