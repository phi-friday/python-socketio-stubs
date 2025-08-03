from collections.abc import Awaitable, Callable, Mapping, Sequence
from contextlib import AbstractAsyncContextManager, AbstractContextManager
from threading import Event as ThreadingEvent
from types import ModuleType
from typing import Any, Literal, TypeAlias, overload

import engineio
from _typeshed import Incomplete
from engineio.async_drivers.eventlet import EventletThread
from engineio.async_drivers.gevent import Thread as GeventThread
from engineio.async_drivers.gevent_uwsgi import Thread as GeventUWSGThread
from engineio.async_drivers.threading import DaemonThread
from engineio.socket import Socket
from gevent.event import Event as GeventEvent
from socketio.admin import InstrumentedServer
from socketio.server import Server
from typing_extensions import NotRequired, Required, TypedDict

JsonType: TypeAlias = (
    str | int | float | bool | None | Sequence[JsonType] | Mapping[str, JsonType]
)
DataType: TypeAlias = str | bytes | Sequence[JsonType] | Mapping[str, JsonType]
TransportType: TypeAlias = Literal["websocket", "polling"]
SocketIOModeType: TypeAlias = Literal["development", "production"]
SyncAsyncModeType: TypeAlias = Literal[
    "eventlet", "gevent_uwsgi", "gevent", "threading"
]
AsyncAsyncModeType: TypeAlias = Literal["aiohttp", "sanic", "tornado", "asgi"]
SerializerType: TypeAlias = Literal["default", "msgpack"]

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

## handlers

ServerConnectHandler: TypeAlias = Callable[[str, dict[str, Any]], Any]
ServerConnectHandlerWithData: TypeAlias = Callable[[str, dict[str, Any], Any], Any]
ServerDisconnectHandler: TypeAlias = Callable[[str, engineio.Server.reason], Any]
ServerDisconnectLegacyHandler: TypeAlias = Callable[[str], Any]
ClientConnectHandler: TypeAlias = Callable[[], Any]
ClientDisconnectHandler: TypeAlias = Callable[[engineio.Client.reason], Any]
ClientDisconnectLegacyHandler: TypeAlias = Callable[[], Any]
ClientConnectErrorHandler: TypeAlias = Callable[[Any], Any]
CatchAllHandler: TypeAlias = Callable[[str, str, Any], Any]
SyncEventHandler: TypeAlias = Callable[
    [str, Any], DataType | tuple[DataType, ...] | None
]
AsyncEventHandler: TypeAlias = Callable[
    [str, Any], Awaitable[DataType | tuple[DataType, ...] | None]
]
EventHandler: TypeAlias = SyncEventHandler | AsyncEventHandler
