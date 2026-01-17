"""Tests for socketio.async_pubsub_manager stub types."""

from __future__ import annotations

import inspect

import socketio.async_manager as async_manager_mod
import socketio.async_pubsub_manager as mod


class TestAsyncPubSubManager:
    """Test AsyncPubSubManager class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "AsyncPubSubManager")
        assert inspect.isclass(mod.AsyncPubSubManager)

    def test_inherits_async_manager(self) -> None:
        assert issubclass(mod.AsyncPubSubManager, async_manager_mod.AsyncManager)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.AsyncPubSubManager.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "channel" in params
        assert "write_only" in params
        assert "logger" in params

    def test_name_attribute(self) -> None:
        assert hasattr(mod.AsyncPubSubManager, "name")

    def test_channel_in_init(self) -> None:
        sig = inspect.signature(mod.AsyncPubSubManager.__init__)
        params = list(sig.parameters.keys())
        assert "channel" in params

    def test_write_only_in_init(self) -> None:
        sig = inspect.signature(mod.AsyncPubSubManager.__init__)
        params = list(sig.parameters.keys())
        assert "write_only" in params

    def test_initialize_method(self) -> None:
        assert hasattr(mod.AsyncPubSubManager, "initialize")
        assert callable(mod.AsyncPubSubManager.initialize)

    def test_emit_method(self) -> None:
        assert hasattr(mod.AsyncPubSubManager, "emit")
        sig = inspect.signature(mod.AsyncPubSubManager.emit)
        params = list(sig.parameters.keys())
        assert "event" in params
        assert "data" in params
        assert "namespace" in params
        assert "room" in params
        assert "skip_sid" in params
        assert "callback" in params
        assert "to" in params

    def test_can_disconnect_method(self) -> None:
        assert hasattr(mod.AsyncPubSubManager, "can_disconnect")
        assert callable(mod.AsyncPubSubManager.can_disconnect)

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.AsyncPubSubManager, "disconnect")
        assert callable(mod.AsyncPubSubManager.disconnect)

    def test_enter_room_method(self) -> None:
        assert hasattr(mod.AsyncPubSubManager, "enter_room")
        assert callable(mod.AsyncPubSubManager.enter_room)

    def test_leave_room_method(self) -> None:
        assert hasattr(mod.AsyncPubSubManager, "leave_room")
        assert callable(mod.AsyncPubSubManager.leave_room)

    def test_close_room_method(self) -> None:
        assert hasattr(mod.AsyncPubSubManager, "close_room")
        assert callable(mod.AsyncPubSubManager.close_room)
