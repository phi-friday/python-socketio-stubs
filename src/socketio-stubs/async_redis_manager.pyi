import logging
from typing import Any

from socketio._types import RedisArgs
from socketio.async_pubsub_manager import AsyncPubSubManager

def parse_redis_sentinel_url(
    url: str,
) -> tuple[list[tuple[str, int]], str | None, RedisArgs]: ...

class AsyncRedisManager(AsyncPubSubManager):
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
