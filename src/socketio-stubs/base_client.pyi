import logging
from collections.abc import Callable
from types import FrameType
from typing import Any, ClassVar, Generic, Literal, overload

import engineio
from _typeshed import Incomplete
from engineio import AsyncClient, Client
from socketio import base_namespace
from socketio._types import TransportType
from typing_extensions import TypeVar

_T_co = TypeVar("_T_co", bound=Client | AsyncClient, covariant=True, default=Any)
_IsAsyncio = TypeVar("_IsAsyncio", bound=bool, default=Literal[False])
_F = TypeVar("_F", bound=Callable[..., Any])

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
    packet_class: Incomplete
    eio: _T_co
    logger: logging.Logger
    connection_url: str | None
    connection_headers: dict[Incomplete, Incomplete] | None
    connection_auth: Incomplete | None
    connection_transports: TransportType | None
    connection_namespaces: list[str]
    socketio_path: str | None
    sid: str | None
    connected: bool
    namespaces: dict[str, str | None]
    handlers: dict[str, Callable[..., Incomplete]]
    namespace_handlers: dict[str, Callable[..., Incomplete]]
    callbacks: dict[str, dict[int, Callable[..., Incomplete]]]
    def __init__(
        self,
        reconnection: bool = ...,
        reconnection_attempts: int = ...,
        reconnection_delay: int = ...,
        reconnection_delay_max: int = ...,
        randomization_factor: float = ...,
        logger: logging.Logger | bool = ...,
        serializer: str = ...,
        json: Incomplete | None = ...,
        handle_sigint: bool = ...,
        **kwargs: Any,
    ) -> None: ...
    def is_asyncio_based(self) -> _IsAsyncio: ...
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
    def get_sid(self, namespace: str | None = ...) -> str | None: ...
    def transport(self) -> TransportType: ...
    def _engineio_client_class(self) -> type[_T_co]: ...
