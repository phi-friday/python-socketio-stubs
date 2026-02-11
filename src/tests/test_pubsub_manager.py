"""Tests for socketio.pubsub_manager stub types."""

from __future__ import annotations

import inspect

import socketio.manager as manager_mod
import socketio.pubsub_manager as mod


class TestPubSubManager:
    """Test PubSubManager class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "PubSubManager")
        assert inspect.isclass(mod.PubSubManager)

    def test_inherits_manager(self) -> None:
        assert issubclass(mod.PubSubManager, manager_mod.Manager)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.PubSubManager.__init__)
        params = list(sig.parameters.keys())
        assert params == ["self", "channel", "write_only", "logger", "json"]

    def test_name_attribute(self) -> None:
        assert hasattr(mod.PubSubManager, "name")

    def test_channel_in_init(self) -> None:
        sig = inspect.signature(mod.PubSubManager.__init__)
        params = list(sig.parameters.keys())
        assert "channel" in params

    def test_write_only_in_init(self) -> None:
        sig = inspect.signature(mod.PubSubManager.__init__)
        params = list(sig.parameters.keys())
        assert "write_only" in params

    def test_initialize_method(self) -> None:
        assert hasattr(mod.PubSubManager, "initialize")
        assert callable(mod.PubSubManager.initialize)

    def test_emit_method(self) -> None:
        assert hasattr(mod.PubSubManager, "emit")
        sig = inspect.signature(mod.PubSubManager.emit)
        params = list(sig.parameters.keys())
        assert "event" in params
        assert "data" in params
        assert "namespace" in params
        assert "room" in params
        assert "skip_sid" in params
        assert "callback" in params
        assert "to" in params

    def test_can_disconnect_method(self) -> None:
        assert hasattr(mod.PubSubManager, "can_disconnect")
        assert callable(mod.PubSubManager.can_disconnect)

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.PubSubManager, "disconnect")
        assert callable(mod.PubSubManager.disconnect)

    def test_enter_room_method(self) -> None:
        assert hasattr(mod.PubSubManager, "enter_room")
        assert callable(mod.PubSubManager.enter_room)

    def test_leave_room_method(self) -> None:
        assert hasattr(mod.PubSubManager, "leave_room")
        assert callable(mod.PubSubManager.leave_room)

    def test_close_room_method(self) -> None:
        assert hasattr(mod.PubSubManager, "close_room")
        assert callable(mod.PubSubManager.close_room)
