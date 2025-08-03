import logging
from collections.abc import Callable
from types import FrameType
from typing import Any, ClassVar, Generic, Literal, overload

import engineio
from engineio.async_client import AsyncClient
from engineio.client import Client
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
from typing_extensions import TypeVar

_T_co = TypeVar("_T_co", bound=Client | AsyncClient, covariant=True, default=Any)
_IsAsyncio = TypeVar("_IsAsyncio", bound=bool, default=Literal[False])
_F = TypeVar("_F", bound=Callable[..., Any])
_F_event = TypeVar("_F_event", bound=EventHandler)
_F_connect = TypeVar("_F_connect", bound=ClientConnectHandler)
_F_connect_error = TypeVar("_F_connect_error", bound=ClientConnectErrorHandler)
_F_disconnect = TypeVar(
    "_F_disconnect", bound=ClientDisconnectHandler | ClientDisconnectLegacyHandler
)
_F_catch_all = TypeVar("_F_catch_all", bound=CatchAllHandler)

default_logger: logging.Logger
reconnecting_clients: list[BaseClient[Any]]

def signal_handler(sig: int, frame: FrameType | None) -> Any: ...

original_signal_handler: Callable[[int, FrameType | None], Any] | None

class BaseClient(Generic[_IsAsyncio, _T_co]):
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
    def on(
        self,
        event: Literal["connect"],
        handler: None = ...,
        namespace: str | None = ...,
    ) -> Callable[[_F_connect], _F_connect]: ...
    @overload
    def on(
        self,
        event: Literal["connect_error"],
        handler: None = ...,
        namespace: str | None = ...,
    ) -> Callable[[_F_connect_error], _F_connect_error]: ...
    @overload
    def on(
        self,
        event: Literal["disconnect"],
        handler: None = ...,
        namespace: str | None = ...,
    ) -> Callable[[_F_disconnect], _F_disconnect]: ...
    @overload
    def on(
        self, event: Literal["*"], handler: None = ..., namespace: str | None = ...
    ) -> Callable[[_F_catch_all], _F_catch_all]: ...
    @overload
    def on(
        self, event: str, handler: None = ..., namespace: str | None = ...
    ) -> Callable[[_F_event], _F_event]: ...
    @overload
    def on(
        self,
        event: Callable[..., Any],
        handler: None = ...,
        namespace: str | None = ...,
    ) -> None: ...
    @overload
    def on(
        self,
        event: str | Callable[..., Any],
        handler: Callable[..., Any] | None = ...,
        namespace: str | None = ...,
    ) -> Callable[[_F], _F] | None: ...
    @overload
    def event(self, handler: EventHandler) -> None: ...
    @overload
    def event(self, namespace: str | None) -> Callable[[_F_event], _F_event]: ...
    def register_namespace(self, namespace_handler: BaseClientNamespace) -> None: ...
    def get_sid(self, namespace: str | None = ...) -> str | None: ...
    def transport(self) -> TransportType: ...
    def _engineio_client_class(self) -> type[_T_co]: ...
