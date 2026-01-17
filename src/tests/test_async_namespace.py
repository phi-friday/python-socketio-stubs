"""Tests for socketio.async_namespace stub types."""

from __future__ import annotations

import inspect

import socketio.async_namespace as mod
import socketio.base_namespace as base_mod


class TestAsyncNamespace:
    """Test AsyncNamespace class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "AsyncNamespace")
        assert inspect.isclass(mod.AsyncNamespace)

    def test_inherits_base_server_namespace(self) -> None:
        assert issubclass(mod.AsyncNamespace, base_mod.BaseServerNamespace)

    def test_trigger_event_method(self) -> None:
        assert hasattr(mod.AsyncNamespace, "trigger_event")
        assert callable(mod.AsyncNamespace.trigger_event)

    def test_emit_method(self) -> None:
        assert hasattr(mod.AsyncNamespace, "emit")
        sig = inspect.signature(mod.AsyncNamespace.emit)
        params = list(sig.parameters.keys())
        # Exact match to catch stub/runtime mismatches
        assert params == [
            "self",
            "event",
            "data",
            "to",
            "room",
            "skip_sid",
            "namespace",
            "callback",
            "ignore_queue",
        ]

    def test_send_method(self) -> None:
        assert hasattr(mod.AsyncNamespace, "send")
        sig = inspect.signature(mod.AsyncNamespace.send)
        params = list(sig.parameters.keys())
        # Exact match to catch stub/runtime mismatches
        assert params == [
            "self",
            "data",
            "to",
            "room",
            "skip_sid",
            "namespace",
            "callback",
            "ignore_queue",
        ]

    def test_call_method(self) -> None:
        assert hasattr(mod.AsyncNamespace, "call")
        sig = inspect.signature(mod.AsyncNamespace.call)
        params = list(sig.parameters.keys())
        # Exact match to catch stub/runtime mismatches
        assert params == [
            "self",
            "event",
            "data",
            "to",
            "sid",
            "namespace",
            "timeout",
            "ignore_queue",
        ]
        # Verify timeout default is None (not int)
        assert sig.parameters["timeout"].default is None

    def test_enter_room_method(self) -> None:
        assert hasattr(mod.AsyncNamespace, "enter_room")
        assert callable(mod.AsyncNamespace.enter_room)

    def test_leave_room_method(self) -> None:
        assert hasattr(mod.AsyncNamespace, "leave_room")
        assert callable(mod.AsyncNamespace.leave_room)

    def test_close_room_method(self) -> None:
        assert hasattr(mod.AsyncNamespace, "close_room")
        assert callable(mod.AsyncNamespace.close_room)

    def test_get_session_method(self) -> None:
        assert hasattr(mod.AsyncNamespace, "get_session")
        assert callable(mod.AsyncNamespace.get_session)

    def test_save_session_method(self) -> None:
        assert hasattr(mod.AsyncNamespace, "save_session")
        assert callable(mod.AsyncNamespace.save_session)

    def test_session_method(self) -> None:
        assert hasattr(mod.AsyncNamespace, "session")
        assert callable(mod.AsyncNamespace.session)

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.AsyncNamespace, "disconnect")
        assert callable(mod.AsyncNamespace.disconnect)


class TestAsyncClientNamespace:
    """Test AsyncClientNamespace class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "AsyncClientNamespace")
        assert inspect.isclass(mod.AsyncClientNamespace)

    def test_inherits_base_client_namespace(self) -> None:
        assert issubclass(mod.AsyncClientNamespace, base_mod.BaseClientNamespace)

    def test_trigger_event_method(self) -> None:
        assert hasattr(mod.AsyncClientNamespace, "trigger_event")
        assert callable(mod.AsyncClientNamespace.trigger_event)

    def test_emit_method(self) -> None:
        assert hasattr(mod.AsyncClientNamespace, "emit")
        sig = inspect.signature(mod.AsyncClientNamespace.emit)
        params = list(sig.parameters.keys())
        # Exact match to catch stub/runtime mismatches
        assert params == ["self", "event", "data", "namespace", "callback"]

    def test_send_method(self) -> None:
        assert hasattr(mod.AsyncClientNamespace, "send")
        sig = inspect.signature(mod.AsyncClientNamespace.send)
        params = list(sig.parameters.keys())
        # Exact match to catch stub/runtime mismatches
        assert params == ["self", "data", "namespace", "callback"]

    def test_call_method(self) -> None:
        assert hasattr(mod.AsyncClientNamespace, "call")
        sig = inspect.signature(mod.AsyncClientNamespace.call)
        params = list(sig.parameters.keys())
        # Exact match to catch stub/runtime mismatches
        assert params == ["self", "event", "data", "namespace", "timeout"]
        # Verify timeout default is None (not int)
        assert sig.parameters["timeout"].default is None

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.AsyncClientNamespace, "disconnect")
        assert callable(mod.AsyncClientNamespace.disconnect)
