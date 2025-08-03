import logging
from collections.abc import Callable, Sequence
from typing import Any

from socketio._types import DataType
from socketio.base_manager import BaseManager

default_logger: logging.Logger

class Manager(BaseManager):
    def can_disconnect(self, sid: str, namespace: str) -> bool: ...
    def emit(
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
    def disconnect(self, sid: str, namespace: str, **kwargs: Any) -> None: ...
    def enter_room(
        self, sid: str, namespace: str, room: str, eio_sid: str | None = None
    ) -> None: ...
    def leave_room(self, sid: str, namespace: str, room: str) -> None: ...
    def close_room(self, room: str, namespace: str) -> None: ...
    def trigger_callback(self, sid: str, id: str, data: Sequence[Any]) -> None: ...
