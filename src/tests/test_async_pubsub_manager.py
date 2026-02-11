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
        # Exact match to catch stub/runtime mismatches
        assert params == ["self", "channel", "write_only", "logger", "json"]

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
        # Exact match to catch stub/runtime mismatches
        assert params == [
            "self",
            "event",
            "data",
            "namespace",
            "room",
            "skip_sid",
            "callback",
            "to",
            "kwargs",
        ]

    def test_can_disconnect_method(self) -> None:
        assert hasattr(mod.AsyncPubSubManager, "can_disconnect")
        sig = inspect.signature(mod.AsyncPubSubManager.can_disconnect)
        params = list(sig.parameters.keys())
        # Exact match to catch stub/runtime mismatches
        assert params == ["self", "sid", "namespace"]

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.AsyncPubSubManager, "disconnect")
        sig = inspect.signature(mod.AsyncPubSubManager.disconnect)
        params = list(sig.parameters.keys())
        # Exact match to catch stub/runtime mismatches
        # namespace is required (no default), not optional
        assert params == ["self", "sid", "namespace", "kwargs"]
        # Verify namespace has no default (is required)
        assert sig.parameters["namespace"].default is inspect.Parameter.empty

    def test_enter_room_method(self) -> None:
        assert hasattr(mod.AsyncPubSubManager, "enter_room")
        assert callable(mod.AsyncPubSubManager.enter_room)

    def test_leave_room_method(self) -> None:
        assert hasattr(mod.AsyncPubSubManager, "leave_room")
        assert callable(mod.AsyncPubSubManager.leave_room)

    def test_close_room_method(self) -> None:
        assert hasattr(mod.AsyncPubSubManager, "close_room")
        assert callable(mod.AsyncPubSubManager.close_room)
