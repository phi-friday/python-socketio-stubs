from .pubsub_manager import PubSubManager as PubSubManager
from _typeshed import Incomplete

logger: Incomplete

def parse_redis_sentinel_url(url): ...

class RedisManager(PubSubManager):
    name: str
    redis_url: Incomplete
    redis_options: Incomplete
    def __init__(self, url: str = 'redis://localhost:6379/0', channel: str = 'socketio', write_only: bool = False, logger=None, redis_options=None) -> None: ...
    def initialize(self) -> None: ...
