"""Tests for socketio.async_server stub types."""

from __future__ import annotations

import inspect
from typing import Any, assert_type

import socketio.async_server as mod
import socketio.base_server as base_mod


class TestTaskReferenceHolder:
    """Test task_reference_holder module attribute."""

    def test_exists(self) -> None:
        assert hasattr(mod, "task_reference_holder")

    def test_type(self) -> None:
        assert_type(mod.task_reference_holder, set[Any])
        assert isinstance(mod.task_reference_holder, set)


class TestAsyncServer:
    """Test AsyncServer class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "AsyncServer")
        assert inspect.isclass(mod.AsyncServer)

    def test_inherits_base_server(self) -> None:
        assert issubclass(mod.AsyncServer, base_mod.BaseServer)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.AsyncServer.__init__)
        params = list(sig.parameters.keys())
        # Exact match to catch stub/runtime mismatches
        assert params == [
            "self",
            "client_manager",
            "logger",
            "json",
            "async_handlers",
            "namespaces",
            "kwargs",
        ]

    def test_attach_method(self) -> None:
        assert hasattr(mod.AsyncServer, "attach")
        assert callable(mod.AsyncServer.attach)

    def test_emit_method(self) -> None:
        assert hasattr(mod.AsyncServer, "emit")
        sig = inspect.signature(mod.AsyncServer.emit)
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
        assert hasattr(mod.AsyncServer, "send")
        assert callable(mod.AsyncServer.send)

    def test_call_method(self) -> None:
        assert hasattr(mod.AsyncServer, "call")
        assert callable(mod.AsyncServer.call)

    def test_enter_room_method(self) -> None:
        assert hasattr(mod.AsyncServer, "enter_room")
        assert callable(mod.AsyncServer.enter_room)

    def test_leave_room_method(self) -> None:
        assert hasattr(mod.AsyncServer, "leave_room")
        assert callable(mod.AsyncServer.leave_room)

    def test_close_room_method(self) -> None:
        assert hasattr(mod.AsyncServer, "close_room")
        assert callable(mod.AsyncServer.close_room)

    def test_get_session_method(self) -> None:
        assert hasattr(mod.AsyncServer, "get_session")
        assert callable(mod.AsyncServer.get_session)

    def test_save_session_method(self) -> None:
        assert hasattr(mod.AsyncServer, "save_session")
        assert callable(mod.AsyncServer.save_session)

    def test_session_method(self) -> None:
        assert hasattr(mod.AsyncServer, "session")
        assert callable(mod.AsyncServer.session)

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.AsyncServer, "disconnect")
        assert callable(mod.AsyncServer.disconnect)

    def test_shutdown_method(self) -> None:
        assert hasattr(mod.AsyncServer, "shutdown")
        assert callable(mod.AsyncServer.shutdown)

    def test_handle_request_method(self) -> None:
        assert hasattr(mod.AsyncServer, "handle_request")
        assert callable(mod.AsyncServer.handle_request)

    def test_start_background_task_method(self) -> None:
        assert hasattr(mod.AsyncServer, "start_background_task")
        assert callable(mod.AsyncServer.start_background_task)

    def test_sleep_method(self) -> None:
        assert hasattr(mod.AsyncServer, "sleep")
        assert callable(mod.AsyncServer.sleep)

    def test_instrument_method(self) -> None:
        assert hasattr(mod.AsyncServer, "instrument")
        assert callable(mod.AsyncServer.instrument)

    def test_register_namespace_method(self) -> None:
        assert hasattr(mod.AsyncServer, "register_namespace")
        assert callable(mod.AsyncServer.register_namespace)
