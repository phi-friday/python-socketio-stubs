import logging
from collections.abc import Callable, Sequence
from typing import Any, Literal

from _typeshed import Incomplete
from socketio import base_manager
from socketio import packet as packet

default_logger: logging.Logger

class Manager(base_manager.BaseManager):
    def can_disconnect(self, sid: str, namespace: str) -> bool: ...
    def emit(
        self,
        event: Literal[0, 1, 2, 3, 4, 5, 6],
        data: tuple[Incomplete, ...] | list[Incomplete] | None,
        namespace: str,
        room: str | None = ...,
        skip_sid: str | list[str] | None = ...,
        callback: Callable[..., Incomplete] | None = ...,
        to: str | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def disconnect(self, sid: str, namespace: str, **kwargs: Any) -> None: ...
    def enter_room(
        self, sid: str, namespace: str, room: str, eio_sid: str | None = None
    ) -> None: ...
    def leave_room(self, sid: str, namespace: str, room: str) -> None: ...
    def close_room(self, room: str, namespace: str) -> None: ...
    def trigger_callback(
        self, sid: str, id: str, data: Sequence[Incomplete]
    ) -> None: ...
