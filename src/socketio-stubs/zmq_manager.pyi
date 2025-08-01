import logging
from collections.abc import Generator

from eventlet.green.zmq import Socket, _Socket_recv
from socketio.pubsub_manager import PubSubManager

class ZmqManager(PubSubManager):
    name: str
    sink: Socket
    sub: Socket
    channel: str
    def __init__(
        self,
        url: str = ...,
        channel: str = ...,
        write_only: bool = ...,
        logger: logging.Logger = ...,
    ) -> None: ...
    def zmq_listen(self) -> Generator[_Socket_recv]: ...
