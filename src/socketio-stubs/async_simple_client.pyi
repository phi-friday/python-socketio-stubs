import asyncio
import types
from typing import Any, ClassVar, Literal, Self

from socketio._types import DataType, TransportType
from socketio.async_client import AsyncClient

class AsyncSimpleClient:
    client_class: ClassVar[type[AsyncClient]]
    client_args: tuple[Any, ...]
    client_kwargs: dict[str, Any]
    client: AsyncClient | None
    namespace: str
    connected_event: asyncio.Event
    connected: bool
    input_event: asyncio.Event
    input_buffer: list[list[Any]]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    async def connect(
        self,
        url: str,
        headers: dict[str, str] = ...,
        auth: Any = ...,
        transports: list[TransportType] | None = ...,
        namespace: str = ...,
        socketio_path: str = ...,
        wait_timeout: int = ...,
    ) -> None: ...
    @property
    def sid(self) -> str | None: ...
    @property
    def transport(self) -> TransportType | Literal[""]: ...
    async def emit(
        self, event: str, data: DataType | tuple[DataType, ...] | None = ...
    ) -> None: ...
    async def call(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None = ...,
        timeout: int = ...,
    ) -> tuple[Any, ...] | None: ...
    async def receive(self, timeout: float | None = ...) -> list[Any]: ...
    async def disconnect(self) -> None: ...
    async def __aenter__(self) -> Self: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> None: ...
