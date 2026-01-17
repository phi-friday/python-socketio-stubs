"""Tests for socketio.namespace stub types."""

from __future__ import annotations

import inspect

import socketio.base_namespace as base_mod
import socketio.namespace as mod


class TestNamespace:
    """Test Namespace class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "Namespace")
        assert inspect.isclass(mod.Namespace)

    def test_inherits_base_server_namespace(self) -> None:
        assert issubclass(mod.Namespace, base_mod.BaseServerNamespace)

    def test_trigger_event_method(self) -> None:
        assert hasattr(mod.Namespace, "trigger_event")
        assert callable(mod.Namespace.trigger_event)

    def test_emit_method(self) -> None:
        assert hasattr(mod.Namespace, "emit")
        sig = inspect.signature(mod.Namespace.emit)
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
        assert hasattr(mod.Namespace, "send")
        assert callable(mod.Namespace.send)

    def test_call_method(self) -> None:
        assert hasattr(mod.Namespace, "call")
        assert callable(mod.Namespace.call)

    def test_enter_room_method(self) -> None:
        assert hasattr(mod.Namespace, "enter_room")
        assert callable(mod.Namespace.enter_room)

    def test_leave_room_method(self) -> None:
        assert hasattr(mod.Namespace, "leave_room")
        assert callable(mod.Namespace.leave_room)

    def test_close_room_method(self) -> None:
        assert hasattr(mod.Namespace, "close_room")
        assert callable(mod.Namespace.close_room)

    def test_get_session_method(self) -> None:
        assert hasattr(mod.Namespace, "get_session")
        assert callable(mod.Namespace.get_session)

    def test_save_session_method(self) -> None:
        assert hasattr(mod.Namespace, "save_session")
        assert callable(mod.Namespace.save_session)

    def test_session_method(self) -> None:
        assert hasattr(mod.Namespace, "session")
        assert callable(mod.Namespace.session)

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.Namespace, "disconnect")
        assert callable(mod.Namespace.disconnect)


class TestClientNamespace:
    """Test ClientNamespace class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "ClientNamespace")
        assert inspect.isclass(mod.ClientNamespace)

    def test_inherits_base_client_namespace(self) -> None:
        assert issubclass(mod.ClientNamespace, base_mod.BaseClientNamespace)

    def test_trigger_event_method(self) -> None:
        assert hasattr(mod.ClientNamespace, "trigger_event")
        assert callable(mod.ClientNamespace.trigger_event)

    def test_emit_method(self) -> None:
        assert hasattr(mod.ClientNamespace, "emit")
        sig = inspect.signature(mod.ClientNamespace.emit)
        params = list(sig.parameters.keys())
        assert "event" in params
        assert "data" in params
        assert "namespace" in params
        assert "callback" in params

    def test_send_method(self) -> None:
        assert hasattr(mod.ClientNamespace, "send")
        assert callable(mod.ClientNamespace.send)

    def test_call_method(self) -> None:
        assert hasattr(mod.ClientNamespace, "call")
        assert callable(mod.ClientNamespace.call)

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.ClientNamespace, "disconnect")
        assert callable(mod.ClientNamespace.disconnect)
