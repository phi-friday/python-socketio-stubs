"""Tests for socketio.server stub types."""

from __future__ import annotations

import inspect
import logging
from typing import assert_type

import socketio.base_server as base_mod
import socketio.server as mod


class TestDefaultLogger:
    """Test default_logger module attribute."""

    def test_exists(self) -> None:
        assert hasattr(mod, "default_logger")

    def test_type(self) -> None:
        assert_type(mod.default_logger, logging.Logger)
        assert isinstance(mod.default_logger, logging.Logger)


class TestServer:
    """Test Server class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "Server")
        assert inspect.isclass(mod.Server)

    def test_inherits_base_server(self) -> None:
        assert issubclass(mod.Server, base_mod.BaseServer)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.Server.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "client_manager" in params
        assert "logger" in params
        assert "serializer" in params
        assert "json" in params
        assert "async_handlers" in params
        assert "always_connect" in params
        assert "namespaces" in params
        # async_mode and engineio options may be in kwargs
        assert "kwargs" in params or any(
            sig.parameters[p].kind == inspect.Parameter.VAR_KEYWORD for p in params
        )

    def test_emit_method(self) -> None:
        assert hasattr(mod.Server, "emit")
        sig = inspect.signature(mod.Server.emit)
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
        assert hasattr(mod.Server, "send")
        assert callable(mod.Server.send)

    def test_call_method(self) -> None:
        assert hasattr(mod.Server, "call")
        assert callable(mod.Server.call)

    def test_enter_room_method(self) -> None:
        assert hasattr(mod.Server, "enter_room")
        assert callable(mod.Server.enter_room)

    def test_leave_room_method(self) -> None:
        assert hasattr(mod.Server, "leave_room")
        assert callable(mod.Server.leave_room)

    def test_close_room_method(self) -> None:
        assert hasattr(mod.Server, "close_room")
        assert callable(mod.Server.close_room)

    def test_get_session_method(self) -> None:
        assert hasattr(mod.Server, "get_session")
        assert callable(mod.Server.get_session)

    def test_save_session_method(self) -> None:
        assert hasattr(mod.Server, "save_session")
        assert callable(mod.Server.save_session)

    def test_session_method(self) -> None:
        assert hasattr(mod.Server, "session")
        assert callable(mod.Server.session)

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.Server, "disconnect")
        assert callable(mod.Server.disconnect)

    def test_shutdown_method(self) -> None:
        assert hasattr(mod.Server, "shutdown")
        assert callable(mod.Server.shutdown)

    def test_handle_request_method(self) -> None:
        assert hasattr(mod.Server, "handle_request")
        assert callable(mod.Server.handle_request)

    def test_start_background_task_method(self) -> None:
        assert hasattr(mod.Server, "start_background_task")
        assert callable(mod.Server.start_background_task)

    def test_sleep_method(self) -> None:
        assert hasattr(mod.Server, "sleep")
        assert callable(mod.Server.sleep)

    def test_instrument_method(self) -> None:
        assert hasattr(mod.Server, "instrument")
        assert callable(mod.Server.instrument)

    def test_register_namespace_method(self) -> None:
        assert hasattr(mod.Server, "register_namespace")
        assert callable(mod.Server.register_namespace)
