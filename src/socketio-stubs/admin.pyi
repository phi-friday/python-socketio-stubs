from collections.abc import Callable, Mapping, Sequence
from typing import Any, Generic

from socketio._types import (
    BufferItem,
    DataType,
    SerializedSocket,
    SocketIOModeType,
    StatsTaskDescriptor,
    StopStateEventDescriptor,
    SyncAsyncModeType,
)
from socketio.server import Server
from typing_extensions import TypeVar

_A = TypeVar("_A", bound=SyncAsyncModeType, default=Any)

HOSTNAME: str
PID: int

class EventBuffer:
    buffer: dict[str, BufferItem]
    def __init__(self) -> None: ...
    def push(self, type: str, count: int = ...) -> None: ...
    def get_and_clear(self) -> list[BufferItem]: ...

class InstrumentedServer(Generic[_A]):
    sio: Server[_A]
    auth: dict[Any, Any] | list[Any] | Callable[[Any], bool]
    admin_namespace: str
    read_only: bool
    server_id: str
    mode: SocketIOModeType
    server_stats_interval: int
    event_buffer: EventBuffer
    stop_stats_event: StopStateEventDescriptor
    stats_task: StatsTaskDescriptor
    def __init__(
        self,
        sio: Server[_A],
        auth: dict[Any, Any] | list[Any] | Callable[[Any], bool] = ...,
        mode: SocketIOModeType = ...,
        read_only: bool = ...,
        server_id: str | None = ...,
        namespace: str = ...,
        server_stats_interval: int = ...,
    ) -> None: ...
    def instrument(self) -> None: ...
    def uninstrument(self) -> None: ...
    def admin_connect(
        self, sid: str, environ: Mapping[str, Any], client_auth: Any
    ) -> None: ...
    def admin_emit(
        self,
        _: Any,
        namespace: str | None,
        room_filter: str | None,
        event: str,
        *data: DataType,
    ) -> None: ...
    def admin_enter_room(
        self,
        _: Any,
        namespace: str | None,
        room: str,
        room_filter: str | Sequence[str] | None = ...,
    ) -> None: ...
    def admin_leave_room(
        self,
        _: Any,
        namespace: str | None,
        room: str,
        room_filter: str | Sequence[str] | None = ...,
    ) -> None: ...
    def admin_disconnect(
        self,
        _: Any,
        namespace: str | None,
        close: Any,
        room_filter: str | Sequence[str] | None = ...,
    ) -> None: ...
    def shutdown(self) -> None: ...
    def serialize_socket(
        self, sid: str, namespace: str, eio_sid: str | None = ...
    ) -> SerializedSocket: ...
