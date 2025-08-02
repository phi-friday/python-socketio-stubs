from collections.abc import Mapping, Sequence
from threading import Event as ThreadingEvent
from typing import Any

from _typeshed import Incomplete
from gevent.event import Event as GeventEvent
from socketio._types import BufferItem, DataType, SerializedSocket, SocketIOModeType
from socketio.server import Server

HOSTNAME: str
PID: int

class EventBuffer:
    buffer: dict[str, BufferItem]
    def __init__(self) -> None: ...
    def push(self, type: str, count: int = ...) -> None: ...
    def get_and_clear(self) -> list[BufferItem]: ...

class InstrumentedServer:
    sio: Server
    auth: Incomplete
    admin_namespace: str
    read_only: bool
    server_id: str
    mode: SocketIOModeType
    server_stats_interval: int
    event_buffer: EventBuffer
    stop_stats_event: ThreadingEvent | GeventEvent | None
    stats_task: Incomplete
    def __init__(
        self,
        sio: Incomplete,
        auth: Incomplete | None = ...,
        mode: SocketIOModeType = ...,
        read_only: bool = ...,
        server_id: str | None = ...,
        namespace: str = ...,
        server_stats_interval: int = ...,
    ) -> None: ...
    def instrument(self) -> None: ...
    def uninstrument(self) -> None: ...
    def admin_connect(
        self, sid: str, environ: Mapping[str, Incomplete], client_auth: Incomplete
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
