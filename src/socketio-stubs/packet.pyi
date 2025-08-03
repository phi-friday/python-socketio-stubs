from typing import Literal

from socketio._types import DataType, JsonModule
from typing_extensions import Buffer

CONNECT: Literal[0]
DISCONNECT: Literal[1]
EVENT: Literal[2]
ACK: Literal[3]
CONNECT_ERROR: Literal[4]
BINARY_EVENT: Literal[5]
BINARY_ACK: Literal[6]
packet_names: list[
    Literal[
        "CONNECT",
        "DISCONNECT",
        "EVENT",
        "ACK",
        "CONNECT_ERROR",
        "BINARY_EVENT",
        "BINARY_ACK",
    ]
]

class Packet:
    uses_binary_events: bool
    json: JsonModule
    packet_type: Literal[0, 1, 2, 3, 4, 5, 6]
    data: list[DataType] | None
    namespace: str | None
    id: str | None
    attachment_count: int
    attachments: list[bytes]
    def __init__(
        self,
        packet_type: Literal[0, 1, 2, 3, 4, 5, 6] = ...,
        data: list[DataType] | None = ...,
        namespace: str | None = ...,
        id: str | None = ...,
        binary: bool | None = ...,
        encoded_packet: Buffer | None = ...,
    ) -> None: ...
    def encode(self) -> DataType: ...
    def decode(self, encoded_packet: Buffer) -> int: ...
    def add_attachment(self, attachment: bytes) -> bool: ...
    def reconstruct_binary(self, attachments: list[bytes]) -> None: ...
