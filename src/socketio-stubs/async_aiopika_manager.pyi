import logging

from aio_pika.abc import (
    AbstractRobustChannel,
    AbstractRobustConnection,
    AbstractRobustExchange,
)
from socketio.async_pubsub_manager import AsyncPubSubManager

class AsyncAioPikaManager(AsyncPubSubManager):
    name: str
    url: str
    publisher_connection: AbstractRobustConnection | None
    publisher_channel: AbstractRobustChannel | None
    publisher_exchange: AbstractRobustExchange | None
    def __init__(
        self,
        url: str = ...,
        channel: str = ...,
        write_only: bool = ...,
        logger: logging.Logger | None = ...,
    ) -> None: ...
