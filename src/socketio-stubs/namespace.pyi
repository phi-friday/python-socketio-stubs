from collections.abc import Callable
from typing import Any, Generic, NoReturn, overload

from _typeshed import Incomplete
from socketio import base_namespace
from socketio._types import DataType, SessionContextManager, SyncAsyncModeType
from socketio.client import Client
from socketio.server import Server
from typing_extensions import TypeVar

_A = TypeVar("_A", bound=SyncAsyncModeType, default=Any)

class Namespace(base_namespace.BaseServerNamespace, Generic[_A]):
    server: Server[_A]  # pyright: ignore[reportIncompatibleVariableOverride]
    def trigger_event(self, event: str, *args: Any) -> Any: ...
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
    def disconnect(self, sid: str, namespace: str | None = ...) -> None: ...

class ClientNamespace(base_namespace.BaseClientNamespace):
    client: Client  # pyright: ignore[reportIncompatibleVariableOverride]
    def trigger_event(self, event: str, *args: Any) -> Any: ...
    def emit(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        namespace: str | None = ...,
        callback: Callable[..., Incomplete] = ...,
    ) -> None: ...
    def send(
        self,
        data: DataType | tuple[DataType, ...] | None,
        namespace: str | None = ...,
        callback: Callable[..., Incomplete] = ...,
    ) -> None: ...
    def call(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        namespace: str | None = ...,
        timeout: int = ...,
    ) -> Incomplete | None: ...
    def disconnect(self) -> None: ...
