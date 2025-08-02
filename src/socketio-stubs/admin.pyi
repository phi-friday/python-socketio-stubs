from collections.abc import Mapping, Sequence
from threading import Event as ThreadingEvent
from typing import Any, Literal

from _typeshed import Incomplete
from gevent.event import Event as GeventEvent
from socketio._types import DataType
from socketio.base_server import BaseServer
from typing_extensions import TypedDict

HOSTNAME: str
PID: int

class _BufferItem(TypedDict, total=True):
    timestamp: int
    type: str
    count: int

class _SerializedSocketHandshake(TypedDict, total=True):
    address: str
    headers: dict[str, Incomplete]
    query: dict[str, str]
    secure: bool
    url: str
    issued: int
    time: str

class _SerializedSocket(TypedDict, total=True):
    id: str
    clientId: str
    transport: Literal["websocket", "polling"]
    nsp: str
    data: dict[Incomplete, Incomplete]
    handshake: _SerializedSocketHandshake
    rooms: list[str]

class EventBuffer:
    buffer: dict[str, _BufferItem]
    def __init__(self) -> None: ...
    def push(self, type: str, count: int = ...) -> None: ...
    def get_and_clear(self) -> list[_BufferItem]: ...

class InstrumentedServer:
    sio: BaseServer[Any]
    auth: Incomplete
    admin_namespace: str
    read_only: bool
    server_id: str
    mode: Literal["development", "production"]
    server_stats_interval: int
    event_buffer: EventBuffer
    stop_stats_event: ThreadingEvent | GeventEvent | None
    stats_task: Incomplete
    def __init__(
        self,
        sio: Incomplete,
        auth: Incomplete | None = ...,
        mode: Literal["development", "production"] = ...,
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
    ) -> _SerializedSocket: ...
