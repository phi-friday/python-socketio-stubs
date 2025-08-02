import logging
from collections.abc import Callable, Mapping
from threading import Thread
from typing import Any, Generic, Literal, NoReturn, ParamSpec, TypeAlias, overload

import engineio
from _typeshed import Incomplete
from socketio import base_server
from socketio._types import (
    SessionContextManager,
    SocketIOModeType,
    SyncAsyncModeType,
    TransportType,
)
from socketio.admin import InstrumentedServer
from socketio.manager import Manager
from typing_extensions import TypeVar

DataType: TypeAlias = str | bytes | list[Incomplete] | dict[Incomplete, Incomplete]
_A = TypeVar("_A", bound=SyncAsyncModeType, default=Any)
_P = ParamSpec("_P")
_T = TypeVar("_T")

default_logger: logging.Logger

class Server(base_server.BaseServer[Literal[False], engineio.Server], Generic[_A]):
    def __init__(
        self,
        client_manager: Manager | None = ...,
        logger: logging.Logger | bool = ...,
        serializer: str = ...,
        json: Incomplete | None = ...,
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
        transport: list[TransportType] | None = ...,
        engineio_logger: logging.Logger | bool = ...,
        **kwargs: Incomplete,
    ) -> None: ...
    def emit(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        to: str | None = ...,
        room: str | None = ...,
        skip_sid: str | list[str] | None = ...,
        namespace: str | None = ...,
        callback: Callable[..., Incomplete] | None = ...,
        ignore_queue: bool = ...,
    ) -> None: ...
    def send(
        self,
        data: DataType | tuple[DataType, ...] | None,
        to: str | None = ...,
        room: str | None = ...,
        skip_sid: str | list[str] | None = ...,
        namespace: str | None = ...,
        callback: Callable[..., Incomplete] | None = ...,
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
    ) -> Incomplete | None: ...
    def enter_room(self, sid: str, room: str, namespace: str | None = ...) -> None: ...
    def leave_room(self, sid: str, room: str, namespace: str | None = ...) -> None: ...
    def close_room(self, room: str, namespace: str | None = ...) -> None: ...
    def get_session(
        self, sid: str, namespace: str | None = ...
    ) -> dict[Incomplete, Incomplete]: ...
    def save_session(
        self,
        sid: str,
        session: dict[Incomplete, Incomplete],
        namespace: str | None = ...,
    ) -> None: ...
    def session(
        self, sid: str, namespace: str | None = ...
    ) -> SessionContextManager: ...
    def disconnect(
        self, sid: str, namespace: str | None = ..., ignore_queue: bool = ...
    ) -> None: ...
    def shutdown(self) -> None: ...
    def handle_request(
        self,
        environ: Mapping[str, Incomplete],
        start_response: Callable[[str, str], Incomplete],
    ) -> list[str | list[tuple[str, str]] | bytes]: ...
    def start_background_task(
        self, target: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs
    ) -> Thread: ...
    def sleep(self, seconds: int = ...) -> None: ...
    def instrument(
        self,
        auth: Incomplete | None = ...,
        mode: SocketIOModeType = ...,
        read_only: bool = ...,
        server_id: str | None = ...,
        namespace: str = ...,
        server_stats_interval: int = ...,
    ) -> InstrumentedServer: ...
