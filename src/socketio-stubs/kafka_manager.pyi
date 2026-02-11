import logging

import kafka

from socketio._types import JsonModule
from socketio.pubsub_manager import PubSubManager

logger: logging.Logger

class KafkaManager(PubSubManager):
    name: str
    kafka_urls: list[str]
    producer: kafka.KafkaProducer
    consumer: kafka.KafkaConsumer
    def __init__(
        self,
        url: str = ...,
        channel: str = ...,
        write_only: bool = ...,
        logger: logging.Logger | None = ...,
        json: JsonModule | None = ...,
    ) -> None: ...
