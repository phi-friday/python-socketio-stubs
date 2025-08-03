import asyncio
from collections.abc import Callable, Mapping, Sequence
from typing import Any, Generic

from socketio._types import (
    AsyncAsyncModeType,
    DataType,
    SerializedSocket,
    SocketIOModeType,
)
from socketio.admin import EventBuffer as EventBuffer
from socketio.async_server import AsyncServer
from typing_extensions import TypeVar

_A = TypeVar("_A", bound=AsyncAsyncModeType, default=Any)

HOSTNAME: str
PID: int

class InstrumentedAsyncServer(Generic[_A]):
    sio: AsyncServer[_A]
    auth: dict[Any, Any] | list[Any] | Callable[[Any], bool]
    admin_namespace: str
    read_only: bool
    server_id: str
    mode: SocketIOModeType
    server_stats_interval: int
    admin_queue: list[tuple[str, tuple[str, str, str, str]]]
    event_buffer: EventBuffer
    stop_stats_event: asyncio.Event | None
    stats_task: asyncio.Task[Any] | None
    def __init__(
        self,
        sio: AsyncServer[_A],
        auth: dict[Any, Any] | list[Any] | Callable[[Any], bool] = ...,
        namespace: str = ...,
        read_only: bool = ...,
        server_id: str | None = ...,
        mode: SocketIOModeType = ...,
        server_stats_interval: int = ...,
    ) -> None: ...
    def instrument(self) -> None: ...
    def uninstrument(self) -> None: ...
    async def admin_connect(
        self, sid: str, environ: Mapping[str, Any], client_auth: Any
    ) -> None: ...
    async def admin_emit(
        self,
        _: Any,
        namespace: str | None,
        room_filter: str | None,
        event: str,
        *data: DataType,
    ) -> None: ...
    async def admin_enter_room(
        self,
        _: Any,
        namespace: str | None,
        room: str,
        room_filter: str | Sequence[str] | None = ...,
    ) -> None: ...
    async def admin_leave_room(
        self,
        _: Any,
        namespace: str | None,
        room: str,
        room_filter: str | Sequence[str] | None = ...,
    ) -> None: ...
    async def admin_disconnect(
        self,
        _: Any,
        namespace: str | None,
        close: Any,
        room_filter: str | Sequence[str] | None = ...,
    ) -> None: ...
    async def shutdown(self) -> None: ...
    def serialize_socket(
        self, sid: str, namespace: str, eio_sid: str | None = ...
    ) -> SerializedSocket: ...
