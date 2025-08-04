import logging
from collections.abc import Callable, Mapping
from threading import Thread
from typing import Any, Generic, Literal, NoReturn, ParamSpec, overload

import engineio
from socketio._types import (
    DataType,
    JsonModule,
    SerializerType,
    SessionContextManager,
    SocketIOModeType,
    SyncAsyncModeType,
    TransportType,
)
from socketio.admin import InstrumentedServer
from socketio.base_server import BaseServer
from socketio.manager import Manager
from socketio.namespace import Namespace
from socketio.packet import Packet
from typing_extensions import TypeVar

_A = TypeVar("_A", bound=SyncAsyncModeType, default=Any)
_P = ParamSpec("_P")
_T = TypeVar("_T")

default_logger: logging.Logger

class Server(BaseServer[Literal[False], engineio.Server], Generic[_A]):
    manager: Manager  # pyright: ignore[reportIncompatibleVariableOverride]
    def __init__(
        self,
        client_manager: Manager | None = ...,
        logger: logging.Logger | bool = ...,
        serializer: SerializerType | type[Packet] = ...,
        json: JsonModule | None = ...,
        async_handlers: bool = ...,
        always_connect: bool = ...,
        namespaces: list[str] | None = ...,
        # engineio options
        *,
        async_mode: _A = ...,
        ping_interval: int = ...,
        ping_timeout: int = ...,
        max_http_buffer_size: int = ...,
        allow_upgrades: bool = ...,
        http_compression: bool = ...,
        compression_threshold: int = ...,
        cookie: str | dict[str, str] | Callable[[], str] | bool | None = ...,
        cors_allowed_origins: str | list[str] | None = ...,
        cors_credentials: bool = ...,
        monitor_clients: bool = ...,
        transports: list[TransportType] | None = ...,
        engineio_logger: logging.Logger | bool = ...,
        **kwargs: Any,
    ) -> None: ...
    def emit(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        to: str | None = ...,
        room: str | None = ...,
        skip_sid: str | list[str] | None = ...,
        namespace: str | None = ...,
        callback: Callable[..., Any] | None = ...,
        ignore_queue: bool = ...,
    ) -> None: ...
    def send(
        self,
        data: DataType | tuple[DataType, ...] | None,
        to: str | None = ...,
        room: str | None = ...,
        skip_sid: str | list[str] | None = ...,
        namespace: str | None = ...,
        callback: Callable[..., Any] | None = ...,
        ignore_queue: bool = ...,
    ) -> None: ...
    @overload
    def call(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        to: None = ...,
        sid: None = ...,
        namespace: str | None = ...,
        timeout: int = ...,
        ignore_queue: bool = ...,
    ) -> NoReturn: ...
    @overload
    def call(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        to: str | None = ...,
        sid: str | None = ...,
        namespace: str | None = ...,
        timeout: int = ...,
        ignore_queue: bool = ...,
    ) -> tuple[Any, ...] | None: ...
    def enter_room(self, sid: str, room: str, namespace: str | None = ...) -> None: ...
    def leave_room(self, sid: str, room: str, namespace: str | None = ...) -> None: ...
    def close_room(self, room: str, namespace: str | None = ...) -> None: ...
    def get_session(self, sid: str, namespace: str | None = ...) -> dict[str, Any]: ...
    def save_session(
        self, sid: str, session: dict[str, Any], namespace: str | None = ...
    ) -> None: ...
    def session(
        self, sid: str, namespace: str | None = ...
    ) -> SessionContextManager: ...
    def disconnect(
        self, sid: str, namespace: str | None = ..., ignore_queue: bool = ...
    ) -> None: ...
    def shutdown(self) -> None: ...
    def handle_request(
        self, environ: Mapping[str, Any], start_response: Callable[[str, str], Any]
    ) -> list[str | list[tuple[str, str]] | bytes]: ...
    def start_background_task(
        self, target: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs
    ) -> Thread: ...
    def sleep(self, seconds: int = ...) -> None: ...
    def instrument(
        self,
        auth: dict[Any, Any] | list[Any] | Callable[[Any], bool] | None = ...,
        mode: SocketIOModeType = ...,
        read_only: bool = ...,
        server_id: str | None = ...,
        namespace: str = ...,
        server_stats_interval: int = ...,
    ) -> InstrumentedServer: ...
    def register_namespace(self, namespace_handler: Namespace) -> None: ...  # pyright: ignore[reportIncompatibleMethodOverride]
