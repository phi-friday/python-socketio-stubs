import asyncio
import logging
from collections.abc import Awaitable, Callable
from typing import Any, Literal, ParamSpec, TypeVar

import engineio
import requests
from socketio._types import DataType, JsonModule, SerializerType, TransportType
from socketio.async_namespace import AsyncClientNamespace
from socketio.base_client import BaseClient
from socketio.packet import Packet

_T = TypeVar("_T")
_P = ParamSpec("_P")

default_logger: logging.Logger

class AsyncClient(BaseClient[Literal[True], engineio.AsyncClient]):
    connection_url: str  # pyright: ignore[reportIncompatibleVariableOverride]
    connection_headers: dict[str, str]  # pyright: ignore[reportIncompatibleVariableOverride]
    connection_auth: Any
    connection_transports: list[TransportType] | None
    connection_namespaces: list[str]
    socketio_path: str  # pyright: ignore[reportIncompatibleVariableOverride]
    namespaces: dict[str, str | None]
    connected: bool

    def __init__(
        self,
        reconnection: bool = ...,
        reconnection_attempts: int = ...,
        reconnection_delay: int = ...,
        reconnection_delay_max: int = ...,
        randomization_factor: float = ...,
        logger: logging.Logger | bool = ...,
        serializer: SerializerType | type[Packet] = ...,
        json: JsonModule | None = ...,
        handle_sigint: bool = ...,
        # engineio options
        *,
        request_timeout: int = ...,
        http_session: requests.Session | None = ...,
        ssl_verify: bool = ...,
        websocket_extra_options: dict[str, Any] | None = ...,
        engineio_logger: logging.Logger | bool = ...,
        **kwargs: Any,
    ) -> None: ...
    async def connect(
        self,
        url: str,
        headers: dict[str, str] = ...,
        auth: Any = ...,
        transports: list[TransportType] | None = ...,
        namespaces: str | list[str] | None = ...,
        socketio_path: str = ...,
        wait: bool = ...,
        wait_timeout: int = ...,
        retry: bool = ...,
    ) -> None: ...
    async def wait(self) -> None: ...
    async def emit(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        namespace: str | None = ...,
        callback: Callable[..., Any] = ...,
    ) -> None: ...
    async def send(
        self,
        data: DataType | tuple[DataType, ...] | None,
        namespace: str | None = ...,
        callback: Callable[..., Any] = ...,
    ) -> None: ...
    async def call(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        namespace: str | None = ...,
        timeout: int = ...,
    ) -> tuple[Any, ...] | None: ...
    async def disconnect(self) -> None: ...
    async def shutdown(self) -> None: ...
    def start_background_task(
        self, target: Callable[_P, Awaitable[_T]], *args: _P.args, **kwargs: _P.kwargs
    ) -> asyncio.Task[_T]: ...
    async def sleep(self, seconds: int = ...) -> None: ...
    def register_namespace(self, namespace_handler: AsyncClientNamespace) -> None: ...  # pyright: ignore[reportIncompatibleMethodOverride]
