"""Tests for socketio.manager stub types."""

from __future__ import annotations

import inspect
import logging
from typing import assert_type

import socketio.base_manager as base_mod
import socketio.manager as mod


class TestDefaultLogger:
    """Test default_logger module attribute."""

    def test_exists(self) -> None:
        assert hasattr(mod, "default_logger")

    def test_type(self) -> None:
        assert_type(mod.default_logger, logging.Logger)
        assert isinstance(mod.default_logger, logging.Logger)


class TestManager:
    """Test Manager class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "Manager")
        assert inspect.isclass(mod.Manager)

    def test_inherits_base_manager(self) -> None:
        assert issubclass(mod.Manager, base_mod.BaseManager)

    def test_can_disconnect_method(self) -> None:
        assert hasattr(mod.Manager, "can_disconnect")
        assert callable(mod.Manager.can_disconnect)

    def test_emit_method(self) -> None:
        assert hasattr(mod.Manager, "emit")
        sig = inspect.signature(mod.Manager.emit)
        params = list(sig.parameters.keys())
        assert "event" in params
        assert "data" in params
        assert "namespace" in params
        assert "room" in params
        assert "skip_sid" in params
        assert "callback" in params
        assert "to" in params

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.Manager, "disconnect")
        assert callable(mod.Manager.disconnect)

    def test_enter_room_method(self) -> None:
        assert hasattr(mod.Manager, "enter_room")
        sig = inspect.signature(mod.Manager.enter_room)
        params = list(sig.parameters.keys())
        assert "sid" in params
        assert "namespace" in params
        assert "room" in params
        assert "eio_sid" in params

    def test_leave_room_method(self) -> None:
        assert hasattr(mod.Manager, "leave_room")
        assert callable(mod.Manager.leave_room)

    def test_close_room_method(self) -> None:
        assert hasattr(mod.Manager, "close_room")
        assert callable(mod.Manager.close_room)

    def test_trigger_callback_method(self) -> None:
        assert hasattr(mod.Manager, "trigger_callback")
        assert callable(mod.Manager.trigger_callback)
