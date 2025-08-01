from .pubsub_manager import PubSubManager as PubSubManager
from _typeshed import Incomplete

class KombuManager(PubSubManager):
    name: str
    url: Incomplete
    connection_options: Incomplete
    exchange_options: Incomplete
    queue_options: Incomplete
    producer_options: Incomplete
    publisher_connection: Incomplete
    def __init__(self, url: str = 'amqp://guest:guest@localhost:5672//', channel: str = 'socketio', write_only: bool = False, logger=None, connection_options=None, exchange_options=None, queue_options=None, producer_options=None) -> None: ...
    def initialize(self) -> None: ...
