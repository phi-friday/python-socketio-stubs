import logging
from collections.abc import Callable
from threading import Thread
from typing import Any

from socketio._types import DataType
from socketio.manager import Manager

class PubSubManager(Manager):
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
    thread: Thread
    def initialize(self) -> None: ...
    def emit(
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
    def can_disconnect(self, sid: str, namespace: str) -> bool: ...
    def disconnect(
        self, sid: str, namespace: str | None = ..., **kwargs: Any
    ) -> None: ...
    def enter_room(
        self, sid: str, namespace: str, room: str, eio_sid: str | None = ...
    ) -> None: ...
    def leave_room(self, sid: str, namespace: str, room: str) -> None: ...
    def close_room(self, room: str, namespace: str | None = ...) -> None: ...
