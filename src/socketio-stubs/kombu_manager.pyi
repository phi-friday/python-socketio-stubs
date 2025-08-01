import logging
from typing import Any

import kombu
from socketio.pubsub_manager import PubSubManager

class KombuManager(PubSubManager):
    name: str
    url: str
    connection_options: dict[str, Any]
    exchange_options: dict[str, Any]
    queue_options: dict[str, Any]
    producer_options: dict[str, Any]
    publisher_connection: kombu.Connection
    def __init__(
        self,
        url: str = ...,
        channel: str = ...,
        write_only: bool = ...,
        logger: logging.Logger | None = ...,
        connection_options: dict[str, Any] | None = ...,
        exchange_options: dict[str, Any] | None = ...,
        queue_options: dict[str, Any] | None = ...,
        producer_options: dict[str, Any] | None = ...,
    ) -> None: ...
    def initialize(self) -> None: ...
