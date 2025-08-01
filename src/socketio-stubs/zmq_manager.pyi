from .pubsub_manager import PubSubManager as PubSubManager
from _typeshed import Incomplete
from collections.abc import Generator

class ZmqManager(PubSubManager):
    name: str
    sink: Incomplete
    sub: Incomplete
    channel: Incomplete
    def __init__(self, url: str = 'zmq+tcp://localhost:5555+5556', channel: str = 'socketio', write_only: bool = False, logger=None) -> None: ...
    def zmq_listen(self) -> Generator[Incomplete]: ...
