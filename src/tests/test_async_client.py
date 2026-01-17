"""Tests for socketio.async_client stub types."""

from __future__ import annotations

import inspect
import logging
from typing import assert_type

import socketio.async_client as mod
import socketio.base_client as base_mod


class TestDefaultLogger:
    """Test default_logger module attribute."""

    def test_exists(self) -> None:
        assert hasattr(mod, "default_logger")

    def test_type(self) -> None:
        assert_type(mod.default_logger, logging.Logger)
        assert isinstance(mod.default_logger, logging.Logger)


class TestAsyncClient:
    """Test AsyncClient class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "AsyncClient")
        assert inspect.isclass(mod.AsyncClient)

    def test_inherits_base_client(self) -> None:
        assert issubclass(mod.AsyncClient, base_mod.BaseClient)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.AsyncClient.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "reconnection" in params
        assert "reconnection_attempts" in params
        assert "reconnection_delay" in params
        assert "reconnection_delay_max" in params
        assert "randomization_factor" in params
        assert "logger" in params
        # additional params may be in kwargs
        assert "kwargs" in params or any(
            sig.parameters[p].kind == inspect.Parameter.VAR_KEYWORD for p in params
        )

    def test_connect_method(self) -> None:
        assert hasattr(mod.AsyncClient, "connect")
        sig = inspect.signature(mod.AsyncClient.connect)
        params = list(sig.parameters.keys())
        assert "url" in params
        assert "headers" in params
        assert "auth" in params
        assert "transports" in params
        assert "namespaces" in params
        assert "socketio_path" in params
        assert "wait" in params
        assert "wait_timeout" in params
        assert "retry" in params

    def test_wait_method(self) -> None:
        assert hasattr(mod.AsyncClient, "wait")
        assert callable(mod.AsyncClient.wait)

    def test_emit_method(self) -> None:
        assert hasattr(mod.AsyncClient, "emit")
        sig = inspect.signature(mod.AsyncClient.emit)
        params = list(sig.parameters.keys())
        assert "event" in params
        assert "data" in params
        assert "namespace" in params
        assert "callback" in params

    def test_send_method(self) -> None:
        assert hasattr(mod.AsyncClient, "send")
        assert callable(mod.AsyncClient.send)

    def test_call_method(self) -> None:
        assert hasattr(mod.AsyncClient, "call")
        assert callable(mod.AsyncClient.call)

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.AsyncClient, "disconnect")
        assert callable(mod.AsyncClient.disconnect)

    def test_shutdown_method(self) -> None:
        assert hasattr(mod.AsyncClient, "shutdown")
        assert callable(mod.AsyncClient.shutdown)

    def test_start_background_task_method(self) -> None:
        assert hasattr(mod.AsyncClient, "start_background_task")
        assert callable(mod.AsyncClient.start_background_task)

    def test_sleep_method(self) -> None:
        assert hasattr(mod.AsyncClient, "sleep")
        assert callable(mod.AsyncClient.sleep)

    def test_register_namespace_method(self) -> None:
        assert hasattr(mod.AsyncClient, "register_namespace")
        assert callable(mod.AsyncClient.register_namespace)
