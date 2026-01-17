"""Tests for socketio.async_admin stub types."""

from __future__ import annotations

import inspect
from typing import assert_type

import socketio.admin as admin_mod
import socketio.async_admin as mod


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


class TestEventBufferReexport:
    """Test EventBuffer re-export."""

    def test_exists(self) -> None:
        assert hasattr(mod, "EventBuffer")

    def test_is_same_as_admin(self) -> None:
        assert mod.EventBuffer is admin_mod.EventBuffer


class TestInstrumentedAsyncServer:
    """Test InstrumentedAsyncServer class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "InstrumentedAsyncServer")
        assert inspect.isclass(mod.InstrumentedAsyncServer)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.InstrumentedAsyncServer.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "sio" in params
        assert "auth" in params
        assert "namespace" in params
        assert "read_only" in params
        assert "server_id" in params
        assert "mode" in params
        assert "server_stats_interval" in params

    def test_instrument_method(self) -> None:
        assert hasattr(mod.InstrumentedAsyncServer, "instrument")
        assert callable(mod.InstrumentedAsyncServer.instrument)

    def test_uninstrument_method(self) -> None:
        assert hasattr(mod.InstrumentedAsyncServer, "uninstrument")
        assert callable(mod.InstrumentedAsyncServer.uninstrument)

    def test_admin_connect_method(self) -> None:
        assert hasattr(mod.InstrumentedAsyncServer, "admin_connect")
        assert callable(mod.InstrumentedAsyncServer.admin_connect)

    def test_admin_emit_method(self) -> None:
        assert hasattr(mod.InstrumentedAsyncServer, "admin_emit")
        assert callable(mod.InstrumentedAsyncServer.admin_emit)

    def test_admin_enter_room_method(self) -> None:
        assert hasattr(mod.InstrumentedAsyncServer, "admin_enter_room")
        assert callable(mod.InstrumentedAsyncServer.admin_enter_room)

    def test_admin_leave_room_method(self) -> None:
        assert hasattr(mod.InstrumentedAsyncServer, "admin_leave_room")
        assert callable(mod.InstrumentedAsyncServer.admin_leave_room)

    def test_admin_disconnect_method(self) -> None:
        assert hasattr(mod.InstrumentedAsyncServer, "admin_disconnect")
        assert callable(mod.InstrumentedAsyncServer.admin_disconnect)

    def test_shutdown_method(self) -> None:
        assert hasattr(mod.InstrumentedAsyncServer, "shutdown")
        assert callable(mod.InstrumentedAsyncServer.shutdown)

    def test_serialize_socket_method(self) -> None:
        assert hasattr(mod.InstrumentedAsyncServer, "serialize_socket")
        assert callable(mod.InstrumentedAsyncServer.serialize_socket)
