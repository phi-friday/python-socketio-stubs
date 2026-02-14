import logging
from collections.abc import Callable
from types import FrameType
from typing import Any, ClassVar, Generic, Literal, overload

import engineio
from engineio.async_client import AsyncClient
from engineio.client import Client
from typing_extensions import TypeVar

from socketio._types import (
    CatchAllHandler,
    ClientConnectErrorHandler,
    ClientConnectHandler,
    ClientDisconnectHandler,
    ClientDisconnectLegacyHandler,
    EventHandler,
    JsonModule,
    SerializerType,
    TransportType,
)
from socketio.base_namespace import BaseClientNamespace
from socketio.packet import Packet

_T_co = TypeVar("_T_co", bound=Client | AsyncClient, covariant=True, default=Any)
_T_namespace = TypeVar(
    "_T_namespace", bound=BaseClientNamespace[Any], default=BaseClientNamespace[Any]
)
_IsAsyncio = TypeVar("_IsAsyncio", bound=bool, default=Literal[False])

default_logger: logging.Logger
reconnecting_clients: list[BaseClient[Any]]

def signal_handler(sig: int, frame: FrameType | None) -> Any: ...

original_signal_handler: Callable[[int, FrameType | None], Any] | None

class BaseClient(Generic[_IsAsyncio, _T_co, _T_namespace]):
    reserved_events: ClassVar[list[str]]
    reason: ClassVar[type[engineio.Client.reason]]
    reconnection: bool
    reconnection_attempts: int
    reconnection_delay: int
    reconnection_delay_max: int
    randomization_factor: float
    handle_sigint: bool
    packet_class: type[Packet]
    eio: _T_co
    logger: logging.Logger
    connection_url: str | None
    connection_headers: dict[str, str] | None
    connection_auth: Any
    connection_transports: list[TransportType] | None
    connection_namespaces: list[str]
    socketio_path: str | None
    sid: str | None
    connected: bool
    failed_namespaces: list[str]
    namespaces: dict[str, str | None]
    handlers: dict[str, Callable[..., Any]]
    namespace_handlers: dict[str, Callable[..., Any]]
    callbacks: dict[str, dict[int, Callable[..., Any]]]
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
        **kwargs: Any,
    ) -> None: ...
    def is_asyncio_based(self) -> _IsAsyncio: ...
    @overload
    def on[H: ClientConnectHandler](
        self,
        event: Literal["connect"],
        handler: None = ...,
        namespace: str | None = ...,
    ) -> Callable[[H], H]: ...
    @overload
    def on[H: ClientConnectErrorHandler](
        self,
        event: Literal["connect_error"],
        handler: None = ...,
        namespace: str | None = ...,
    ) -> Callable[[H], H]: ...
    @overload
    def on[H: ClientDisconnectHandler | ClientDisconnectLegacyHandler](
        self,
        event: Literal["disconnect"],
        handler: None = ...,
        namespace: str | None = ...,
    ) -> Callable[[H], H]: ...
    @overload
    def on[H: CatchAllHandler](
        self, event: Literal["*"], handler: None = ..., namespace: str | None = ...
    ) -> Callable[[H], H]: ...
    @overload
    def on[H: EventHandler](
        self, event: str, handler: None = ..., namespace: str | None = ...
    ) -> Callable[[H], H]: ...
    @overload
    def on(
        self,
        event: Callable[..., Any],
        handler: None = ...,
        namespace: str | None = ...,
    ) -> None: ...
    @overload
    def on[F: Callable[..., Any]](
        self,
        event: str | Callable[..., Any],
        handler: Callable[..., Any] | None = ...,
        namespace: str | None = ...,
    ) -> Callable[[F], F] | None: ...
    @overload
    def event(self, handler: EventHandler) -> None: ...
    @overload
    def event[H: EventHandler](self, namespace: str | None) -> Callable[[H], H]: ...
    def register_namespace(self, namespace_handler: _T_namespace) -> None: ...
    def get_sid(self, namespace: str | None = ...) -> str | None: ...
    def transport(self) -> TransportType: ...
    def _engineio_client_class(self) -> type[_T_co]: ...
