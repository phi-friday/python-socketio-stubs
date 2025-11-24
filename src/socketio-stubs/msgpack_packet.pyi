from collections.abc import Callable
from typing import Any

from typing_extensions import Buffer

from socketio._types import CustomMsgPackPacket
from socketio.packet import Packet

class MsgPackPacket(Packet):
    uses_binary_events: bool
    def encode(self) -> bytes: ...
    def decode(self, encoded_packet: Buffer) -> None: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    @classmethod
    def configure(
        cls,
        dumps_default: Callable[[Any], Any] | None = ...,
        ext_hook: Callable[[int, bytes], Any] = ...,
    ) -> type[CustomMsgPackPacket]: ...
