from contextlib import AbstractContextManager
from typing import Any, Literal, TypeAlias

from _typeshed import Incomplete
from engineio.socket import Socket
from socketio.server import Server
from typing_extensions import NotRequired, Required, TypedDict

DataType: TypeAlias = str | bytes | list[Incomplete] | dict[Incomplete, Incomplete]
TransportType: TypeAlias = Literal["websocket", "polling"]
SocketIOModeType: TypeAlias = Literal["development", "production"]
AsyncModeType: TypeAlias = Literal["eventlet", "gevent_uwsgi", "gevent", "threading"]

class SessionContextManager(AbstractContextManager[Socket]):
    server: Server
    sid: str
    namespace: str | None
    session: Socket | None

    def __enter__(self) -> Socket: ...
    def __exit__(self, *args: object, **kwargs: Any) -> None: ...

class BufferItem(TypedDict, total=True):
    timestamp: int
    type: str
    count: int

class SerializedSocketHandshake(TypedDict, total=True):
    address: str
    headers: dict[str, Incomplete]
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
