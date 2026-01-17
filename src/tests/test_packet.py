"""Tests for socketio.packet stub types."""

from __future__ import annotations

import inspect
from typing import Literal, assert_type

import socketio.packet as mod


class TestPacketConstants:
    """Test packet type constants."""

    def test_connect_exists(self) -> None:
        assert hasattr(mod, "CONNECT")
        assert_type(mod.CONNECT, Literal[0])
        assert mod.CONNECT == 0

    def test_disconnect_exists(self) -> None:
        assert hasattr(mod, "DISCONNECT")
        assert_type(mod.DISCONNECT, Literal[1])
        assert mod.DISCONNECT == 1

    def test_event_exists(self) -> None:
        assert hasattr(mod, "EVENT")
        assert_type(mod.EVENT, Literal[2])
        assert mod.EVENT == 2

    def test_ack_exists(self) -> None:
        assert hasattr(mod, "ACK")
        assert_type(mod.ACK, Literal[3])
        assert mod.ACK == 3

    def test_connect_error_exists(self) -> None:
        assert hasattr(mod, "CONNECT_ERROR")
        assert_type(mod.CONNECT_ERROR, Literal[4])
        assert mod.CONNECT_ERROR == 4

    def test_binary_event_exists(self) -> None:
        assert hasattr(mod, "BINARY_EVENT")
        assert_type(mod.BINARY_EVENT, Literal[5])
        assert mod.BINARY_EVENT == 5

    def test_binary_ack_exists(self) -> None:
        assert hasattr(mod, "BINARY_ACK")
        assert_type(mod.BINARY_ACK, Literal[6])
        assert mod.BINARY_ACK == 6


class TestPacketNames:
    """Test packet_names list."""

    def test_exists(self) -> None:
        assert hasattr(mod, "packet_names")

    def test_is_list(self) -> None:
        assert isinstance(mod.packet_names, list)

    def test_length(self) -> None:
        assert len(mod.packet_names) == 7

    def test_values(self) -> None:
        expected = [
            "CONNECT",
            "DISCONNECT",
            "EVENT",
            "ACK",
            "CONNECT_ERROR",
            "BINARY_EVENT",
            "BINARY_ACK",
        ]
        assert mod.packet_names == expected


class TestPacket:
    """Test Packet class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "Packet")
        assert inspect.isclass(mod.Packet)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.Packet.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "packet_type" in params
        assert "data" in params
        assert "namespace" in params
        assert "id" in params
        assert "binary" in params
        assert "encoded_packet" in params

    def test_uses_binary_events_attribute(self) -> None:
        packet = mod.Packet()
        assert hasattr(packet, "uses_binary_events")
        assert_type(packet.uses_binary_events, bool)
        assert isinstance(packet.uses_binary_events, bool)

    def test_packet_type_attribute(self) -> None:
        packet = mod.Packet(packet_type=mod.EVENT)
        assert hasattr(packet, "packet_type")
        assert isinstance(packet.packet_type, int)

    def test_encode_method(self) -> None:
        packet = mod.Packet(packet_type=mod.EVENT, data=["test", "data"])
        assert hasattr(packet, "encode")
        assert callable(packet.encode)

    def test_decode_method(self) -> None:
        packet = mod.Packet()
        assert hasattr(packet, "decode")
        assert callable(packet.decode)

    def test_add_attachment_method(self) -> None:
        packet = mod.Packet()
        assert hasattr(packet, "add_attachment")
        assert callable(packet.add_attachment)

    def test_reconstruct_binary_classmethod(self) -> None:
        assert hasattr(mod.Packet, "reconstruct_binary")
        assert callable(mod.Packet.reconstruct_binary)

    def test_deconstruct_binary_classmethod(self) -> None:
        assert hasattr(mod.Packet, "deconstruct_binary")
        assert callable(mod.Packet.deconstruct_binary)

    def test_data_is_binary_classmethod(self) -> None:
        assert hasattr(mod.Packet, "data_is_binary")
        assert callable(mod.Packet.data_is_binary)
