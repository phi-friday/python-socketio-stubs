import asyncio
import logging
from collections.abc import Callable
from typing import Any

from socketio._types import DataType
from socketio.async_manager import AsyncManager

class AsyncPubSubManager(AsyncManager):
    name: str
    channel: str
    write_only: bool
    host_id: str
    logger: logging.Logger | None
    def __init__(
        self,
        channel: str = ...,
        write_only: bool = ...,
        logger: logging.Logger | None = ...,
    ) -> None: ...
    thread: asyncio.Task[Any]
    def initialize(self) -> None: ...
    async def emit(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None,
        namespace: str | None = ...,
        room: str | None = ...,
        skip_sid: str | list[str] | None = ...,
        callback: Callable[..., Any] | None = ...,
        to: str | None = ...,
        **kwargs: Any,
    ) -> None: ...
    async def can_disconnect(self, sid: str, namespace: str) -> bool: ...
    async def disconnect(
        self, sid: str, namespace: str | None = ..., **kwargs: Any
    ) -> None: ...
    async def enter_room(
        self, sid: str, namespace: str, room: str, eio_sid: str | None = ...
    ) -> None: ...
    async def leave_room(self, sid: str, namespace: str, room: str) -> None: ...
    async def close_room(self, room: str, namespace: str | None = ...) -> None: ...
