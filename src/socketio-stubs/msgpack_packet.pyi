from socketio.packet import Packet
from typing_extensions import Buffer

class MsgPackPacket(Packet):
    uses_binary_events: bool
    def encode(self) -> bytes: ...
    def decode(self, encoded_packet: Buffer) -> None: ...  # pyright: ignore[reportIncompatibleMethodOverride]
