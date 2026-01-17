"""Tests for socketio.msgpack_packet stub types."""

from __future__ import annotations

import inspect

import socketio.msgpack_packet as mod
import socketio.packet as packet_mod


class TestMsgPackPacket:
    """Test MsgPackPacket class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "MsgPackPacket")
        assert inspect.isclass(mod.MsgPackPacket)

    def test_inherits_packet(self) -> None:
        assert issubclass(mod.MsgPackPacket, packet_mod.Packet)

    def test_uses_binary_events_attribute(self) -> None:
        assert hasattr(mod.MsgPackPacket, "uses_binary_events")

    def test_encode_method(self) -> None:
        assert hasattr(mod.MsgPackPacket, "encode")
        assert callable(mod.MsgPackPacket.encode)

    def test_decode_method(self) -> None:
        assert hasattr(mod.MsgPackPacket, "decode")
        assert callable(mod.MsgPackPacket.decode)

    def test_configure_classmethod(self) -> None:
        assert hasattr(mod.MsgPackPacket, "configure")
        assert callable(mod.MsgPackPacket.configure)

    def test_configure_signature(self) -> None:
        sig = inspect.signature(mod.MsgPackPacket.configure)
        params = list(sig.parameters.keys())
        assert "dumps_default" in params
        assert "ext_hook" in params
