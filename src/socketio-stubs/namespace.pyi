from collections.abc import Callable
from typing import Any, Generic, Literal, NoReturn, overload

from socketio._types import DataType, SessionContextManager, SyncAsyncModeType
from socketio.base_namespace import BaseClientNamespace, BaseServerNamespace
from socketio.client import Client
from socketio.server import Server
from typing_extensions import TypeVar

_A = TypeVar("_A", bound=SyncAsyncModeType, default=Any)

class Namespace(BaseServerNamespace[Literal[False]], Generic[_A]):
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
        callback: Callable[..., Any] | None = ...,
        ignore_queue: bool = ...,
    ) -> None: ...
    def send(
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
    ) -> tuple[Any, ...] | None: ...
    def enter_room(self, sid: str, room: str, namespace: str | None = ...) -> None: ...
    def leave_room(self, sid: str, room: str, namespace: str | None = ...) -> None: ...
    def close_room(self, room: str, namespace: str | None = ...) -> None: ...
    def get_session(self, sid: str, namespace: str | None = ...) -> dict[str, Any]: ...
    def save_session(
        self, sid: str, session: dict[str, Any], namespace: str | None = ...
    ) -> None: ...
    def session(
        self, sid: str, namespace: str | None = ...
    ) -> SessionContextManager: ...
    def disconnect(self, sid: str, namespace: str | None = ...) -> None: ...

class ClientNamespace(BaseClientNamespace[Literal[False]]):
    client: Client  # pyright: ignore[reportIncompatibleVariableOverride]
    def trigger_event(self, event: str, *args: Any) -> Any: ...
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
