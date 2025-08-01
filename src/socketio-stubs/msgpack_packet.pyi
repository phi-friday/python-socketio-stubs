from _typeshed import Incomplete
from socketio import packet
from typing_extensions import Buffer

class MsgPackPacket(packet.Packet):
    uses_binary_events: bool
    def encode(self) -> bytes: ...
    packet_type: Incomplete
    data: Incomplete
    id: Incomplete
    namespace: Incomplete
    def decode(self, encoded_packet: Buffer) -> None: ...  # pyright: ignore[reportIncompatibleMethodOverride]
