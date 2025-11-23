from collections.abc import Callable
from typing import Any

from socketio._types import CustomMsgPackPacket
from socketio.packet import Packet
from typing_extensions import Buffer

class MsgPackPacket(Packet):
    uses_binary_events: bool
    def encode(self) -> bytes: ...
    def decode(self, encoded_packet: Buffer) -> None: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    @classmethod
    def configure(
        cls,
        dump_default: Callable[[Any], Any] | None = ...,
        ext_hook: Callable[[int, bytes], Any] = ...,
    ) -> type[CustomMsgPackPacket]: ...
