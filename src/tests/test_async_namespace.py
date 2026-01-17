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
        assert "event" in params
        assert "data" in params
        assert "to" in params
        assert "room" in params
        assert "skip_sid" in params
        assert "namespace" in params
        assert "callback" in params
        assert "ignore_queue" in params

    def test_send_method(self) -> None:
        assert hasattr(mod.AsyncNamespace, "send")
        assert callable(mod.AsyncNamespace.send)

    def test_call_method(self) -> None:
        assert hasattr(mod.AsyncNamespace, "call")
        assert callable(mod.AsyncNamespace.call)

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
        assert "event" in params
        assert "data" in params
        assert "namespace" in params
        assert "callback" in params

    def test_send_method(self) -> None:
        assert hasattr(mod.AsyncClientNamespace, "send")
        assert callable(mod.AsyncClientNamespace.send)

    def test_call_method(self) -> None:
        assert hasattr(mod.AsyncClientNamespace, "call")
        assert callable(mod.AsyncClientNamespace.call)

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.AsyncClientNamespace, "disconnect")
        assert callable(mod.AsyncClientNamespace.disconnect)
