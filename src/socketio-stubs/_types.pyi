from contextlib import AbstractContextManager
from typing import Any, TypeAlias

from _typeshed import Incomplete
from engineio.socket import Socket
from socketio.server import Server

DataType: TypeAlias = str | bytes | list[Incomplete] | dict[Incomplete, Incomplete]

class SessionContextManager(AbstractContextManager[Socket]):
    server: Server
    sid: str
    namespace: str | None
    session: Socket | None

    def __enter__(self) -> Socket: ...
    def __exit__(self, *args: object, **kwargs: Any) -> None: ...
