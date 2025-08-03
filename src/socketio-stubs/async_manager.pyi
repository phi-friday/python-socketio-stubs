from collections.abc import Callable, Sequence
from typing import Any

from socketio._types import DataType
from socketio.base_manager import BaseManager

class AsyncManager(BaseManager):
    async def can_disconnect(self, sid: str, namespace: str) -> bool: ...
    async def emit(
        self,
        event: str,
        data: DataType | tuple[DataType, ...] | None,
        namespace: str,
        room: str | None = ...,
        skip_sid: str | list[str] | None = ...,
        callback: Callable[..., Any] | None = ...,
        to: str | None = ...,
        **kwargs: Any,
    ) -> None: ...
    async def connect(self, eio_sid: str, namespace: str) -> str: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    async def disconnect(self, sid: str, namespace: str, **kwargs: Any) -> None: ...
    async def enter_room(
        self, sid: str, namespace: str, room: str, eio_sid: str | None = None
    ) -> None: ...
    async def leave_room(self, sid: str, namespace: str, room: str) -> None: ...
    async def close_room(self, room: str, namespace: str) -> None: ...
    async def trigger_callback(
        self, sid: str, id: str, data: Sequence[Any]
    ) -> None: ...
