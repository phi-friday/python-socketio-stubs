import logging
from typing import Any

from socketio._types import RedisArgs
from socketio.pubsub_manager import PubSubManager

logger: logging.Logger

def parse_redis_sentinel_url(
    url: str,
) -> tuple[list[tuple[str, int]], str | None, RedisArgs]: ...

class RedisManager(PubSubManager):
    name: str
    redis_url: str
    redis_options: dict[str, Any]
    def __init__(
        self,
        url: str = ...,
        channel: str = ...,
        write_only: bool = ...,
        logger: logging.Logger | None = ...,
        redis_options: dict[str, Any] | None = ...,
    ) -> None: ...
    def initialize(self) -> None: ...
