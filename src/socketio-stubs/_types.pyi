from collections.abc import Awaitable, Callable, Mapping, Sequence
from contextlib import AbstractAsyncContextManager, AbstractContextManager
from threading import Event as ThreadingEvent
from types import ModuleType
from typing import Any, ClassVar, Concatenate, Literal, NotRequired, Required, overload

import engineio
from _typeshed import Incomplete
from engineio.async_drivers.eventlet import EventletThread
from engineio.async_drivers.gevent import Thread as GeventThread
from engineio.async_drivers.gevent_uwsgi import Thread as GeventUWSGThread
from engineio.async_drivers.threading import DaemonThread
from engineio.socket import Socket
from gevent.event import Event as GeventEvent
from typing_extensions import TypedDict

from socketio.admin import InstrumentedServer
from socketio.msgpack_packet import MsgPackPacket
from socketio.server import Server

type JsonType = (
    str | int | float | bool | None | Sequence[JsonType] | Mapping[str, JsonType]
)
type DataType = str | bytes | Sequence[JsonType] | Mapping[str, JsonType]
type TransportType = Literal["websocket", "polling"]
type SocketIOModeType = Literal["development", "production"]
type SyncAsyncModeType = Literal["eventlet", "gevent_uwsgi", "gevent", "threading"]
type AsyncAsyncModeType = Literal["aiohttp", "sanic", "tornado", "asgi"]
type SerializerType = Literal["default", "msgpack"]

class SessionContextManager(AbstractContextManager[Socket]):
    server: Server[Any]
    sid: str
    namespace: str | None
    session: Socket | None

    def __enter__(self) -> Socket: ...
    def __exit__(self, *args: object, **kwargs: Any) -> None: ...

class AsyncSessionContextManager(AbstractAsyncContextManager[Socket]):
    server: Server[Any]
    sid: str
    namespace: str | None
    session: Socket | None

    async def __aenter__(self) -> Socket: ...
    async def __aexit__(self, *args: object, **kwargs: Any) -> None: ...

class BufferItem(TypedDict, total=True):
    timestamp: int
    type: str
    count: int

class SerializedSocketHandshake(TypedDict, total=True):
    address: str
    headers: dict[str, str]
    query: dict[str, str]
    secure: bool
    url: str
    issued: int
    time: str

class SerializedSocket(TypedDict, total=True):
    id: str
    clientId: str
    transport: TransportType
    nsp: str
    data: dict[Incomplete, Incomplete]
    handshake: SerializedSocketHandshake
    rooms: list[str]

class ErrorArgs(TypedDict, total=False):
    message: Required[str]
    data: NotRequired[Any]

class RedisArgs(TypedDict, total=False):
    username: str
    password: str
    db: int

class StopStateEventDescriptor:
    @overload
    def __get__(
        self,
        instance: InstrumentedServer[Literal["gevent_uwsgi"]],
        owner: type[InstrumentedServer[Any]],
    ) -> GeventEvent | None: ...
    @overload
    def __get__(
        self,
        instance: InstrumentedServer[Literal["gevent"]],
        owner: type[InstrumentedServer[Any]],
    ) -> GeventEvent | None: ...
    @overload
    def __get__(
        self,
        instance: InstrumentedServer[Literal["eventlet"]],
        owner: type[InstrumentedServer[Any]],
    ) -> ThreadingEvent | None: ...
    @overload
    def __get__(
        self,
        instance: InstrumentedServer[Literal["threading"]],
        owner: type[InstrumentedServer[Any]],
    ) -> ThreadingEvent | None: ...
    @overload
    def __get__(
        self,
        instance: InstrumentedServer[SyncAsyncModeType],
        owner: type[InstrumentedServer[SyncAsyncModeType]],
    ) -> ThreadingEvent | GeventEvent | None: ...
    @overload
    def __set__(
        self,
        instance: InstrumentedServer[Literal["gevent_uwsgi"]],
        value: GeventEvent | None,
    ) -> None: ...
    @overload
    def __set__(
        self, instance: InstrumentedServer[Literal["gevent"]], value: GeventEvent | None
    ) -> None: ...
    @overload
    def __set__(
        self,
        instance: InstrumentedServer[Literal["eventlet"]],
        value: ThreadingEvent | None,
    ) -> None: ...
    @overload
    def __set__(
        self,
        instance: InstrumentedServer[Literal["threading"]],
        value: ThreadingEvent | None,
    ) -> None: ...
    @overload
    def __set__(
        self,
        instance: InstrumentedServer[SyncAsyncModeType],
        value: ThreadingEvent | GeventEvent | None,
    ) -> None: ...
    def __delete__(self, instance: InstrumentedServer[Any]) -> None: ...

class StatsTaskDescriptor:
    @overload
    def __get__(
        self,
        instance: InstrumentedServer[Literal["eventlet"]],
        owner: type[InstrumentedServer[Literal["eventlet"]]],
    ) -> EventletThread | None: ...
    @overload
    def __get__(
        self,
        instance: InstrumentedServer[Literal["gevent_uwsgi"]],
        owner: type[InstrumentedServer[Literal["gevent_uwsgi",]]],
    ) -> GeventUWSGThread | None: ...
    @overload
    def __get__(
        self,
        instance: InstrumentedServer[Literal["gevent"]],
        owner: type[InstrumentedServer[Literal["gevent"]]],
    ) -> GeventThread | None: ...
    @overload
    def __get__(
        self,
        instance: InstrumentedServer[Literal["threading"]],
        owner: type[InstrumentedServer[Literal["threading"]]],
    ) -> DaemonThread | None: ...
    @overload
    def __get__(
        self,
        instance: InstrumentedServer[SyncAsyncModeType],
        owner: type[InstrumentedServer[SyncAsyncModeType]],
    ) -> EventletThread | GeventUWSGThread | GeventThread | DaemonThread | None: ...
    @overload
    def __set__(
        self,
        instance: InstrumentedServer[Literal["eventlet",]],
        value: EventletThread | None,
    ) -> None: ...
    @overload
    def __set__(
        self,
        instance: InstrumentedServer[Literal["gevent_uwsgi"]],
        value: GeventUWSGThread | None,
    ) -> None: ...
    @overload
    def __set__(
        self,
        instance: InstrumentedServer[Literal["gevent"]],
        value: GeventThread | None,
    ) -> None: ...
    @overload
    def __set__(
        self,
        instance: InstrumentedServer[Literal["threading"]],
        value: DaemonThread | None,
    ) -> None: ...
    @overload
    def __set__(
        self,
        instance: InstrumentedServer[SyncAsyncModeType],
        value: EventletThread | GeventUWSGThread | GeventThread | DaemonThread | None,
    ) -> None: ...
    def __delete__(self, instance: InstrumentedServer[Any]) -> None: ...

class JsonModule(ModuleType):
    @staticmethod
    def dumps(obj: Any, **kwargs: Any) -> str: ...
    @staticmethod
    def loads(s: str | bytes | bytearray, **kwargs: Any) -> Any: ...

class CustomMsgPackPacket(MsgPackPacket):
    dumps_default: ClassVar[Callable[[Any], Any] | None]
    ext_hook: ClassVar[Callable[[int, bytes], Any]]

## handlers

type ServerConnectHandler = Callable[[str, dict[str, Any]], Any]
type ServerConnectHandlerWithData = Callable[[str, dict[str, Any], Any], Any]
type ServerDisconnectHandler = Callable[[str, engineio.Server.reason], Any]
type ServerDisconnectLegacyHandler = Callable[[str], Any]
type ClientConnectHandler = Callable[[], Any]
type ClientDisconnectHandler = Callable[[engineio.Client.reason], Any]
type ClientDisconnectLegacyHandler = Callable[[], Any]
type ClientConnectErrorHandler = Callable[[Any], Any]
type CatchAllHandler = Callable[[str, str, Any], Any]
type SyncEventHandlerWithSid = Callable[
    Concatenate[str, ...], DataType | tuple[DataType, ...] | None
]
type SyncEventHandlerWithoutSid = Callable[[], DataType | tuple[DataType, ...] | None]
type SyncEventHandler = SyncEventHandlerWithSid | SyncEventHandlerWithoutSid
type AsyncEventHandlerWithSid = Callable[
    Concatenate[str, ...], Awaitable[DataType | tuple[DataType, ...] | None]
]
type AsyncEventHandlerWithoutSid = Callable[
    [], Awaitable[DataType | tuple[DataType, ...] | None]
]
type AsyncEventHandler = AsyncEventHandlerWithSid | AsyncEventHandlerWithoutSid
type EventHandler = SyncEventHandler | AsyncEventHandler
