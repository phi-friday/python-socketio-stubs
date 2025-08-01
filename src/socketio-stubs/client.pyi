from collections.abc import Callable
from threading import Thread
from typing import Literal, ParamSpec, TypeVar

import engineio
from _typeshed import Incomplete
from socketio import base_client
from socketio._types import DataType

_T = TypeVar("_T")
_P = ParamSpec("_P")

class Client(base_client.BaseClient[engineio.Client]):
    connection_url: str  # pyright: ignore[reportIncompatibleVariableOverride]
    connection_headers: dict[Incomplete, Incomplete]  # pyright: ignore[reportIncompatibleVariableOverride]
    connection_auth: Incomplete | None
    connection_transports: Literal["polling", "websocket"] | None
    connection_namespaces: list[str]
    socketio_path: str  # pyright: ignore[reportIncompatibleVariableOverride]
    namespaces: dict[str, str | None]
    connected: bool
    def connect(
        self,
        url: str,
        headers: dict[Incomplete, Incomplete] = ...,
        auth: Incomplete | None = ...,
        transports: Literal["polling", "websocket"] | None = ...,
        namespaces: str | list[str] | None = ...,
        socketio_path: str = ...,
        wait: bool = ...,
        wait_timeout: int = ...,
        retry: bool = ...,
    ) -> None: ...
    def wait(self) -> None: ...
    def emit(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        namespace: str | None = ...,
        callback: Callable[..., Incomplete] = ...,
    ) -> None: ...
    def send(
        self,
        data: DataType | tuple[DataType, ...] | None,
        namespace: str | None = ...,
        callback: Callable[..., Incomplete] = ...,
    ) -> None: ...
    def call(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        namespace: str | None = ...,
        timeout: int = ...,
    ) -> Incomplete | None: ...
    def disconnect(self) -> None: ...
    def shutdown(self) -> None: ...
    def start_background_task(
        self, target: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs
    ) -> Thread: ...
    def sleep(self, seconds: int = ...) -> None: ...
