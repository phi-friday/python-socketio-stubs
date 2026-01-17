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
        assert hasattr(mod.Namespace, "send")
        sig = inspect.signature(mod.Namespace.send)
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
        assert hasattr(mod.Namespace, "call")
        sig = inspect.signature(mod.Namespace.call)
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
        # Exact match to catch stub/runtime mismatches
        assert params == ["self", "event", "data", "namespace", "callback"]

    def test_send_method(self) -> None:
        assert hasattr(mod.ClientNamespace, "send")
        sig = inspect.signature(mod.ClientNamespace.send)
        params = list(sig.parameters.keys())
        # Exact match to catch stub/runtime mismatches
        assert params == ["self", "data", "room", "namespace", "callback"]

    def test_call_method(self) -> None:
        assert hasattr(mod.ClientNamespace, "call")
        sig = inspect.signature(mod.ClientNamespace.call)
        params = list(sig.parameters.keys())
        # Exact match to catch stub/runtime mismatches
        assert params == ["self", "event", "data", "namespace", "timeout"]
        # Verify timeout default is None (not int)
        assert sig.parameters["timeout"].default is None

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.ClientNamespace, "disconnect")
        assert callable(mod.ClientNamespace.disconnect)
