from .async_pubsub_manager import AsyncPubSubManager as AsyncPubSubManager
from .redis_manager import parse_redis_sentinel_url as parse_redis_sentinel_url
from _typeshed import Incomplete

class AsyncRedisManager(AsyncPubSubManager):
    name: str
    redis_url: Incomplete
    redis_options: Incomplete
    def __init__(self, url: str = 'redis://localhost:6379/0', channel: str = 'socketio', write_only: bool = False, logger=None, redis_options=None) -> None: ...
