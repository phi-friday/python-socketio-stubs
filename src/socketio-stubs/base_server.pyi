import logging
from collections.abc import Callable, Mapping
from typing import Any, ClassVar, Generic, Literal, overload

import engineio
from engineio.async_server import AsyncServer
from engineio.server import Server
from socketio._types import (
    CatchAllHandler,
    EventHandler,
    JsonModule,
    SerializerType,
    ServerConnectHandler,
    ServerConnectHandlerWithData,
    ServerDisconnectHandler,
    ServerDisconnectLegacyHandler,
    SyncAsyncModeType,
    TransportType,
)
from socketio.base_manager import BaseManager
from socketio.base_namespace import BaseClientNamespace
from socketio.packet import Packet
from typing_extensions import TypeVar

_T_co = TypeVar("_T_co", bound=Server | AsyncServer, covariant=True, default=Any)
_F = TypeVar("_F", bound=Callable[..., Any])
_F_event = TypeVar("_F_event", bound=EventHandler)
_F_connect = TypeVar(
    "_F_connect", bound=ServerConnectHandler | ServerConnectHandlerWithData
)
_F_disconnect = TypeVar(
    "_F_disconnect", bound=ServerDisconnectHandler | ServerDisconnectLegacyHandler
)
_F_catch_all = TypeVar("_F_catch_all", bound=CatchAllHandler)
_IsAsyncio = TypeVar("_IsAsyncio", bound=bool, default=Literal[False])

default_logger: logging.Logger

class BaseServer(Generic[_IsAsyncio, _T_co]):
    reserved_events: ClassVar[list[str]]
    reason: ClassVar[type[engineio.Server.reason]]
    packet_class: type[Packet]
    eio: _T_co
    environ: Mapping[str, Any]
    handlers: Callable[..., Any]
    namespace_handlers: dict[str, Callable[..., Any]]
    not_handled: object
    logger: logging.Logger
    manager: BaseManager
    manager_initialized: bool
    async_handlers: bool
    always_connect: bool
    namespaces: list[str]
    async_mode: SyncAsyncModeType
    def __init__(
        self,
        client_manager: BaseManager | None = ...,
        logger: logging.Logger | bool = ...,
        serializer: SerializerType | type[Packet] = ...,
        json: JsonModule | None = ...,
        async_handlers: bool = ...,
        always_connect: bool = ...,
        namespaces: list[str] | None = ...,
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
    def event(self, handler: EventHandler, namespace: str | None = ...) -> None: ...
    @overload
    def event(self, namespace: str | None) -> Callable[[_F_event], _F_event]: ...
    def register_namespace(
        self, namespace_handler: BaseClientNamespace[_IsAsyncio]
    ) -> None: ...
    def rooms(self, sid: str, namespace: str | None = ...) -> str | list[str]: ...
    def transport(self, sid: str, namespace: str | None = ...) -> TransportType: ...
    def get_environ(
        self, sid: str, namespace: str | None = ...
    ) -> Mapping[str, Any] | None: ...
