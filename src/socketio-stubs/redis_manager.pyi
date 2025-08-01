import logging
from typing import Any

from _typeshed import Incomplete
from socketio.pubsub_manager import PubSubManager
from typing_extensions import TypedDict

logger: Incomplete

class _RedisArgs(TypedDict, total=False):
    username: str
    password: str
    db: int

def parse_redis_sentinel_url(
    url: str,
) -> tuple[list[tuple[str, int]], str | None, _RedisArgs]: ...

class RedisManager(PubSubManager):
    name: str
    redis_url: str
    redis_options: Incomplete
    def __init__(
        self,
        url: str = ...,
        channel: str = ...,
        write_only: bool = ...,
        logger: logging.Logger | None = ...,
        redis_options: dict[str, Any] | None = ...,
    ) -> None: ...
    def initialize(self) -> None: ...
