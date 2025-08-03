import logging
from collections.abc import Callable
from threading import Thread
from typing import Any, Literal, ParamSpec, TypeVar

import engineio
import requests
from socketio._types import DataType, JsonModule, SerializerType, TransportType
from socketio.base_client import BaseClient
from socketio.namespace import ClientNamespace
from socketio.packet import Packet

_T = TypeVar("_T")
_P = ParamSpec("_P")

class Client(BaseClient[Literal[False], engineio.Client]):
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
    def connect(
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
    def wait(self) -> None: ...
    def emit(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        namespace: str | None = ...,
        callback: Callable[..., Any] = ...,
    ) -> None: ...
    def send(
        self,
        data: DataType | tuple[DataType, ...] | None,
        namespace: str | None = ...,
        callback: Callable[..., Any] = ...,
    ) -> None: ...
    def call(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        namespace: str | None = ...,
        timeout: int = ...,
    ) -> tuple[Any, ...] | None: ...
    def disconnect(self) -> None: ...
    def shutdown(self) -> None: ...
    def start_background_task(
        self, target: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs
    ) -> Thread: ...
    def sleep(self, seconds: int = ...) -> None: ...
    def register_namespace(self, namespace_handler: ClientNamespace) -> None: ...  # pyright: ignore[reportIncompatibleMethodOverride]
