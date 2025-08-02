from typing import Any, Generic

from _typeshed import Incomplete
from socketio.base_client import BaseClient
from socketio.base_server import BaseServer
from typing_extensions import TypeVar

_Async = TypeVar("_Async", bound=bool, default=Any)

class BaseNamespace(Generic[_Async]):
    namespace: str
    def __init__(self, namespace: str | None = ...) -> None: ...
    def is_asyncio_based(self) -> _Async: ...

class BaseServerNamespace(BaseNamespace[_Async], Generic[_Async]):
    server: BaseServer[_Async, Any] | None
    def __init__(self, namespace: str | None = ...) -> None: ...
    def rooms(self, sid: str, namespace: str | None = ...) -> Incomplete: ...
    def _set_server(self, server: BaseServer[_Async, Any]) -> None: ...

class BaseClientNamespace(BaseNamespace[_Async], Generic[_Async]):
    client: BaseClient[_Async, Any] | None
    def __init__(self, namespace: str | None = ...) -> None: ...
    def _set_client(self, client: BaseClient[_Async, Any]) -> None: ...
