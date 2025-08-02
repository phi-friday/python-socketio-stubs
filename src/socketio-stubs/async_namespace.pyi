from collections.abc import Callable
from typing import Any, Generic, Literal, NoReturn, overload

from _typeshed import Incomplete
from socketio._types import AsyncAsyncModeType, AsyncSessionContextManager, DataType
from socketio.async_client import AsyncClient
from socketio.async_server import AsyncServer
from socketio.base_namespace import BaseClientNamespace, BaseServerNamespace
from typing_extensions import TypeVar

_A = TypeVar("_A", bound=AsyncAsyncModeType, default=Any)

class AsyncNamespace(BaseServerNamespace[Literal[True]], Generic[_A]):
    server: AsyncServer[_A]  # pyright: ignore[reportIncompatibleVariableOverride]
    async def trigger_event(self, event: str, *args: Any) -> Any: ...
    async def emit(
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
    async def send(
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
    async def call(
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
    async def call(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        to: str | None = ...,
        sid: str | None = ...,
        namespace: str | None = ...,
        timeout: int = ...,
        ignore_queue: bool = ...,
    ) -> Incomplete | None: ...
    async def enter_room(
        self, sid: str, room: str, namespace: str | None = ...
    ) -> None: ...
    async def leave_room(
        self, sid: str, room: str, namespace: str | None = ...
    ) -> None: ...
    async def close_room(self, room: str, namespace: str | None = ...) -> None: ...
    async def get_session(
        self, sid: str, namespace: str | None = ...
    ) -> dict[Incomplete, Incomplete]: ...
    async def save_session(
        self,
        sid: str,
        session: dict[Incomplete, Incomplete],
        namespace: str | None = ...,
    ) -> None: ...
    def session(
        self, sid: str, namespace: str | None = ...
    ) -> AsyncSessionContextManager: ...
    async def disconnect(self, sid: str, namespace: str | None = ...) -> None: ...

class AsyncClientNamespace(BaseClientNamespace[Literal[True]]):
    client: AsyncClient  # pyright: ignore[reportIncompatibleVariableOverride]
    async def trigger_event(self, event: str, *args: Any) -> Any: ...
    async def emit(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        namespace: str | None = ...,
        callback: Callable[..., Incomplete] = ...,
    ) -> None: ...
    async def send(
        self,
        data: DataType | tuple[DataType, ...] | None,
        namespace: str | None = ...,
        callback: Callable[..., Incomplete] = ...,
    ) -> None: ...
    async def call(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        namespace: str | None = ...,
        timeout: int = ...,
    ) -> Incomplete | None: ...
    async def disconnect(self) -> None: ...
