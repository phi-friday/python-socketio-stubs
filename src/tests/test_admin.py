"""Tests for socketio.admin stub types."""

from __future__ import annotations

import inspect
from typing import assert_type

import socketio.admin as mod


class TestModuleConstants:
    """Test module-level constants."""

    def test_hostname_exists(self) -> None:
        assert hasattr(mod, "HOSTNAME")

    def test_hostname_type(self) -> None:
        assert_type(mod.HOSTNAME, str)
        assert isinstance(mod.HOSTNAME, str)

    def test_pid_exists(self) -> None:
        assert hasattr(mod, "PID")

    def test_pid_type(self) -> None:
        assert_type(mod.PID, int)
        assert isinstance(mod.PID, int)


class TestEventBuffer:
    """Test EventBuffer class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "EventBuffer")
        assert inspect.isclass(mod.EventBuffer)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.EventBuffer.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params

    def test_buffer_attribute(self) -> None:
        buf = mod.EventBuffer()
        assert hasattr(buf, "buffer")
        assert isinstance(buf.buffer, dict)

    def test_push_method(self) -> None:
        assert hasattr(mod.EventBuffer, "push")
        sig = inspect.signature(mod.EventBuffer.push)
        params = list(sig.parameters.keys())
        assert "type" in params
        assert "count" in params

    def test_get_and_clear_method(self) -> None:
        assert hasattr(mod.EventBuffer, "get_and_clear")
        assert callable(mod.EventBuffer.get_and_clear)


class TestInstrumentedServer:
    """Test InstrumentedServer class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "InstrumentedServer")
        assert inspect.isclass(mod.InstrumentedServer)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.InstrumentedServer.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "sio" in params
        assert "auth" in params
        assert "mode" in params
        assert "read_only" in params
        assert "server_id" in params
        assert "namespace" in params
        assert "server_stats_interval" in params

    def test_instrument_method(self) -> None:
        assert hasattr(mod.InstrumentedServer, "instrument")
        assert callable(mod.InstrumentedServer.instrument)

    def test_uninstrument_method(self) -> None:
        assert hasattr(mod.InstrumentedServer, "uninstrument")
        assert callable(mod.InstrumentedServer.uninstrument)

    def test_admin_connect_method(self) -> None:
        assert hasattr(mod.InstrumentedServer, "admin_connect")
        assert callable(mod.InstrumentedServer.admin_connect)

    def test_admin_emit_method(self) -> None:
        assert hasattr(mod.InstrumentedServer, "admin_emit")
        assert callable(mod.InstrumentedServer.admin_emit)

    def test_admin_enter_room_method(self) -> None:
        assert hasattr(mod.InstrumentedServer, "admin_enter_room")
        assert callable(mod.InstrumentedServer.admin_enter_room)

    def test_admin_leave_room_method(self) -> None:
        assert hasattr(mod.InstrumentedServer, "admin_leave_room")
        assert callable(mod.InstrumentedServer.admin_leave_room)

    def test_admin_disconnect_method(self) -> None:
        assert hasattr(mod.InstrumentedServer, "admin_disconnect")
        assert callable(mod.InstrumentedServer.admin_disconnect)

    def test_shutdown_method(self) -> None:
        assert hasattr(mod.InstrumentedServer, "shutdown")
        assert callable(mod.InstrumentedServer.shutdown)

    def test_serialize_socket_method(self) -> None:
        assert hasattr(mod.InstrumentedServer, "serialize_socket")
        assert callable(mod.InstrumentedServer.serialize_socket)
