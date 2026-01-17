"""Tests for socketio.async_manager stub types."""

from __future__ import annotations

import inspect

import socketio.async_manager as mod
import socketio.base_manager as base_mod


class TestAsyncManager:
    """Test AsyncManager class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "AsyncManager")
        assert inspect.isclass(mod.AsyncManager)

    def test_inherits_base_manager(self) -> None:
        assert issubclass(mod.AsyncManager, base_mod.BaseManager)

    def test_can_disconnect_method(self) -> None:
        assert hasattr(mod.AsyncManager, "can_disconnect")
        assert callable(mod.AsyncManager.can_disconnect)

    def test_emit_method(self) -> None:
        assert hasattr(mod.AsyncManager, "emit")
        sig = inspect.signature(mod.AsyncManager.emit)
        params = list(sig.parameters.keys())
        assert "event" in params
        assert "data" in params
        assert "namespace" in params
        assert "room" in params
        assert "skip_sid" in params
        assert "callback" in params
        assert "to" in params

    def test_connect_method(self) -> None:
        assert hasattr(mod.AsyncManager, "connect")
        assert callable(mod.AsyncManager.connect)

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.AsyncManager, "disconnect")
        assert callable(mod.AsyncManager.disconnect)

    def test_enter_room_method(self) -> None:
        assert hasattr(mod.AsyncManager, "enter_room")
        sig = inspect.signature(mod.AsyncManager.enter_room)
        params = list(sig.parameters.keys())
        assert "sid" in params
        assert "namespace" in params
        assert "room" in params
        assert "eio_sid" in params

    def test_leave_room_method(self) -> None:
        assert hasattr(mod.AsyncManager, "leave_room")
        assert callable(mod.AsyncManager.leave_room)

    def test_close_room_method(self) -> None:
        assert hasattr(mod.AsyncManager, "close_room")
        assert callable(mod.AsyncManager.close_room)

    def test_trigger_callback_method(self) -> None:
        assert hasattr(mod.AsyncManager, "trigger_callback")
        assert callable(mod.AsyncManager.trigger_callback)
