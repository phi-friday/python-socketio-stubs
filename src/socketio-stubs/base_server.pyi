import logging
from collections.abc import Callable, Mapping
from typing import Any, ClassVar, Generic, overload

import engineio
from _typeshed import Incomplete
from engineio import AsyncServer, Server
from socketio import base_namespace
from socketio._types import SyncAsyncModeType, TransportType
from socketio.manager import Manager
from typing_extensions import TypeVar

_T_co = TypeVar("_T_co", bound=Server | AsyncServer, covariant=True, default=Any)
_F = TypeVar("_F", bound=Callable[..., Any])

default_logger: logging.Logger

class BaseServer(Generic[_T_co]):
    reserved_events: ClassVar[list[str]]
    reason: ClassVar[type[engineio.Client.reason]]
    packet_class: Incomplete
    eio: _T_co
    environ: Mapping[str, Incomplete]
    handlers: Callable[..., Incomplete]
    namespace_handlers: dict[str, Callable[..., Incomplete]]
    not_handled: object
    logger: logging.Logger
    manager: Manager
    manager_initialized: bool
    async_handlers: bool
    always_connect: bool
    namespaces: list[str]
    async_mode: SyncAsyncModeType
    def __init__(
        self,
        client_manager: Manager | None = ...,
        logger: logging.Logger | bool = ...,
        serializer: str = ...,
        json: Incomplete | None = ...,
        async_handlers: bool = ...,
        always_connect: bool = ...,
        namespaces: list[str] | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def is_asyncio_based(self) -> bool: ...
    @overload
    def on(
        self,
        event: Callable[..., Incomplete],
        handler: None = ...,
        namespace: None = ...,
    ) -> None: ...
    @overload
    def on(
        self,
        event: str,
        handler: Callable[..., Incomplete],
        namespace: str | None = ...,
    ) -> Callable[[_F], _F] | None: ...
    @overload
    def on(
        self,
        event: str | Callable[..., Incomplete],
        handler: Callable[..., Incomplete] | None = ...,
        namespace: str | None = ...,
    ) -> Callable[[_F], _F] | None: ...
    @overload
    def event(self, handler: Callable[..., Incomplete]) -> None: ...
    @overload
    def event(
        self, handler: Callable[..., Incomplete], namespace: str | None
    ) -> Callable[[_F], _F]: ...
    @overload
    def event(
        self, handler: Callable[..., Incomplete], namespace: str | None = ...
    ) -> Callable[[_F], _F] | None: ...
    def register_namespace(
        self, namespace_handler: base_namespace.BaseClientNamespace
    ) -> None: ...
    def rooms(self, sid: str, namespace: str | None = ...) -> str | list[str]: ...
    def transport(self, sid: str, namespace: str | None = ...) -> TransportType: ...
    def get_environ(
        self, sid: str, namespace: str | None = ...
    ) -> Incomplete | None: ...
