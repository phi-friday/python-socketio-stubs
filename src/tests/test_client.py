"""Tests for socketio.client stub types."""

from __future__ import annotations

import inspect

import socketio.base_client as base_mod
import socketio.client as mod


class TestClient:
    """Test Client class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "Client")
        assert inspect.isclass(mod.Client)

    def test_inherits_base_client(self) -> None:
        assert issubclass(mod.Client, base_mod.BaseClient)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.Client.__init__)
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
        assert hasattr(mod.Client, "connect")
        sig = inspect.signature(mod.Client.connect)
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
        assert hasattr(mod.Client, "wait")
        assert callable(mod.Client.wait)

    def test_emit_method(self) -> None:
        assert hasattr(mod.Client, "emit")
        sig = inspect.signature(mod.Client.emit)
        params = list(sig.parameters.keys())
        assert "event" in params
        assert "data" in params
        assert "namespace" in params
        assert "callback" in params

    def test_send_method(self) -> None:
        assert hasattr(mod.Client, "send")
        assert callable(mod.Client.send)

    def test_call_method(self) -> None:
        assert hasattr(mod.Client, "call")
        assert callable(mod.Client.call)

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.Client, "disconnect")
        assert callable(mod.Client.disconnect)

    def test_shutdown_method(self) -> None:
        assert hasattr(mod.Client, "shutdown")
        assert callable(mod.Client.shutdown)

    def test_start_background_task_method(self) -> None:
        assert hasattr(mod.Client, "start_background_task")
        assert callable(mod.Client.start_background_task)

    def test_sleep_method(self) -> None:
        assert hasattr(mod.Client, "sleep")
        assert callable(mod.Client.sleep)

    def test_register_namespace_method(self) -> None:
        assert hasattr(mod.Client, "register_namespace")
        assert callable(mod.Client.register_namespace)
