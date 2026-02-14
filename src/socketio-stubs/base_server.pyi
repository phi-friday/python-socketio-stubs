import logging
from collections.abc import Callable, Mapping
from typing import Any, ClassVar, Generic, Literal, overload

import engineio
from engineio.async_server import AsyncServer
from engineio.server import Server
from typing_extensions import TypeVar

from socketio._types import (
    CatchAllHandler,
    EventHandler,
    JsonModule,
    SerializerType,
    ServerConnectHandler,
    ServerDisconnectHandler,
    SyncAsyncModeType,
    TransportType,
)
from socketio.base_manager import BaseManager
from socketio.base_namespace import BaseClientNamespace
from socketio.packet import Packet

_T_co = TypeVar("_T_co", bound=Server | AsyncServer, covariant=True, default=Any)
_IsAsyncio = TypeVar("_IsAsyncio", bound=bool, default=Literal[False])

default_logger: logging.Logger

class BaseServer(Generic[_IsAsyncio, _T_co]):
    reserved_events: ClassVar[list[str]]
    reason: ClassVar[type[engineio.Server.reason]]
    packet_class: type[Packet]
    eio: _T_co
    environ: Mapping[str, Any]
    handlers: dict[str, Callable[..., Any]]
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
    def on[H: ServerConnectHandler](
        self,
        event: Literal["connect"],
        handler: None = ...,
        namespace: str | None = ...,
    ) -> Callable[[H], H]: ...
    @overload
    def on[H: ServerDisconnectHandler](
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
    def event(self, handler: EventHandler, namespace: str | None = ...) -> None: ...
    @overload
    def event[H: EventHandler](self, namespace: str | None) -> Callable[[H], H]: ...
    def register_namespace(
        self, namespace_handler: BaseClientNamespace[_IsAsyncio]
    ) -> None: ...
    def rooms(self, sid: str, namespace: str | None = ...) -> str | list[str]: ...
    def transport(self, sid: str, namespace: str | None = ...) -> TransportType: ...
    def get_environ(
        self, sid: str, namespace: str | None = ...
    ) -> Mapping[str, Any] | None: ...
