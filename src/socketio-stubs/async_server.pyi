import asyncio
import logging
from collections.abc import Awaitable, Callable, Iterable, Mapping, Sequence
from typing import Any, Generic, Literal, NoReturn, ParamSpec, overload

import engineio
from aiohttp.typedefs import LooseHeaders as AiohttpLooseHeaders
from aiohttp.web import Application as AiohttpApplication
from aiohttp.web import Response as AiohttpResponse
from engineio.async_drivers.asgi import ASGIApp as EngineIOASGIApp
from sanic import Sanic
from sanic.response import HTTPResponse as SanicHTTPResponse
from socketio._types import (
    AsyncAsyncModeType,
    AsyncSessionContextManager,
    DataType,
    JsonModule,
    SerializerType,
    SocketIOModeType,
    TransportType,
)
from socketio.asgi import ASGIApp as SocketIOASGIApp
from socketio.async_admin import InstrumentedAsyncServer
from socketio.async_manager import AsyncManager
from socketio.async_namespace import AsyncNamespace
from socketio.base_server import BaseServer
from socketio.packet import Packet
from tornado.web import Application as TornadoApplication
from typing_extensions import TypeVar

_A = TypeVar("_A", bound=AsyncAsyncModeType, default=Any)
_P = ParamSpec("_P")
_T = TypeVar("_T")

task_reference_holder: set[Any]

class AsyncServer(BaseServer[Literal[True], engineio.AsyncServer], Generic[_A]):
    manager: AsyncManager  # pyright: ignore[reportIncompatibleVariableOverride]
    def __init__(
        self,
        client_manager: AsyncManager | None = ...,
        logger: logging.Logger | bool = ...,
        serializer: SerializerType | type[Packet] = ...,
        json: JsonModule | None = ...,
        async_handlers: bool = ...,
        always_connect: bool = ...,
        namespaces: list[str] | None = ...,
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
    @overload
    def attach(
        self: AsyncServer[Literal["aiohttp"]],
        app: AiohttpApplication,
        socketio_path: str = ...,
    ) -> None: ...
    @overload
    def attach(
        self: AsyncServer[Literal["sanic"]],
        app: Sanic[Any, Any],
        socketio_path: str = ...,
    ) -> None: ...
    @overload
    def attach(
        self: AsyncServer[Literal["asgi"]],
        app: EngineIOASGIApp | SocketIOASGIApp,
        socketio_path: str = ...,
    ) -> None: ...
    @overload
    def attach(
        self: AsyncServer[Literal["tornado"]],
        app: TornadoApplication,
        socketio_path: str = ...,
    ) -> None: ...
    @overload
    def attach(
        self,
        app: AiohttpApplication
        | Sanic[Any, Any]
        | EngineIOASGIApp
        | TornadoApplication
        | SocketIOASGIApp,
        socketio_path: str = ...,
    ) -> None: ...
    async def emit(
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
    async def send(
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
    async def call(
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
    async def call(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        to: str | None = ...,
        sid: str | None = ...,
        namespace: str | None = ...,
        timeout: int = ...,
        ignore_queue: bool = ...,
    ) -> tuple[Any, ...] | None: ...
    async def enter_room(
        self, sid: str, room: str, namespace: str | None = ...
    ) -> None: ...
    async def leave_room(
        self, sid: str, room: str, namespace: str | None = ...
    ) -> None: ...
    async def close_room(self, room: str, namespace: str | None = ...) -> None: ...
    async def get_session(
        self, sid: str, namespace: str | None = ...
    ) -> dict[str, Any]: ...
    async def save_session(
        self, sid: str, session: dict[str, Any], namespace: str | None = ...
    ) -> None: ...
    def session(
        self, sid: str, namespace: str | None = ...
    ) -> AsyncSessionContextManager: ...
    async def disconnect(
        self, sid: str, namespace: str | None = ..., ignore_queue: bool = ...
    ) -> None: ...
    async def shutdown(self) -> None: ...
    @overload
    async def handle_request(
        self: AsyncServer[Literal["aiohttp"]],
        status: str = ...,
        headers: AiohttpLooseHeaders | None = ...,
        payload: Any = ...,
        environ: Mapping[str, Any] = ...,
    ) -> AiohttpResponse: ...
    @overload
    async def handle_request(
        self: AsyncServer[Literal["asgi"]],
        state: str = ...,
        headers: Iterable[Sequence[str]] = ...,
        playload: Any = ...,
        environ: Mapping[str, Any] = ...,
    ) -> None: ...
    @overload
    async def handle_request(
        self: AsyncServer[Literal["sanic"]],
        state: str = ...,
        headers: Iterable[Sequence[str]] = ...,
        playload: Any = ...,
        environ: Mapping[str, Any] = ...,
    ) -> SanicHTTPResponse: ...
    @overload
    async def handle_request(
        self: AsyncServer[Literal["tornado"]],
        state: str = ...,
        headers: Iterable[Sequence[str]] = ...,
        playload: Any = ...,
        environ: Mapping[str, Any] = ...,
    ) -> None: ...
    @overload
    async def handle_request(
        self, *args: Any, **kwargs: Any
    ) -> AiohttpResponse | SanicHTTPResponse | None: ...
    def start_background_task(
        self, target: Callable[_P, Awaitable[_T]], *args: _P.args, **kwargs: _P.kwargs
    ) -> asyncio.Task[_T]: ...
    async def sleep(self, seconds: int = ...) -> None: ...
    def instrument(
        self,
        auth: dict[Any, Any] | list[Any] | Callable[[Any], bool] = ...,
        mode: SocketIOModeType = ...,
        read_only: bool = ...,
        server_id: str | None = ...,
        namespace: str = ...,
        server_stats_interval: int = ...,
    ) -> InstrumentedAsyncServer: ...
    def register_namespace(self, namespace_handler: AsyncNamespace) -> None: ...  # pyright: ignore[reportIncompatibleMethodOverride]
