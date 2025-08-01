from . import base_namespace as base_namespace, manager as manager, packet as packet
from _typeshed import Incomplete

default_logger: Incomplete

class BaseServer:
    reserved_events: Incomplete
    reason: Incomplete
    packet_class: Incomplete
    eio: Incomplete
    environ: Incomplete
    handlers: Incomplete
    namespace_handlers: Incomplete
    not_handled: Incomplete
    logger: Incomplete
    manager: Incomplete
    manager_initialized: bool
    async_handlers: Incomplete
    always_connect: Incomplete
    namespaces: Incomplete
    async_mode: Incomplete
    def __init__(self, client_manager=None, logger: bool = False, serializer: str = 'default', json=None, async_handlers: bool = True, always_connect: bool = False, namespaces=None, **kwargs) -> None: ...
    def is_asyncio_based(self): ...
    def on(self, event, handler=None, namespace=None): ...
    def event(self, *args, **kwargs): ...
    def register_namespace(self, namespace_handler) -> None: ...
    def rooms(self, sid, namespace=None): ...
    def transport(self, sid, namespace=None): ...
    def get_environ(self, sid, namespace=None): ...
