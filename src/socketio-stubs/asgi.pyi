from collections.abc import Callable
from typing import Any

import engineio
from socketio.async_server import AsyncServer

class ASGIApp(engineio.ASGIApp):
    def __init__(
        self,
        socketio_server: AsyncServer,
        other_asgi_app: Any = ...,
        static_files: dict[str, dict[str, str]] | None = ...,
        socketio_path: str = ...,
        on_startup: Callable[[], Any] | None = ...,
        on_shutdown: Callable[[], Any] | None = ...,
    ) -> None: ...
