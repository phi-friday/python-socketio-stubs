"""Tests for socketio.simple_client stub types."""

from __future__ import annotations

import inspect
from threading import Event
from typing import assert_type

import socketio.client as client_mod
import socketio.simple_client as mod


class TestSimpleClient:
    """Test SimpleClient class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "SimpleClient")
        assert inspect.isclass(mod.SimpleClient)

    def test_client_class_class_var(self) -> None:
        assert hasattr(mod.SimpleClient, "client_class")
        assert mod.SimpleClient.client_class is client_mod.Client

    def test_init_accepts_any_args(self) -> None:
        sig = inspect.signature(mod.SimpleClient.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "args" in params
        assert "kwargs" in params

    def test_connect_method(self) -> None:
        assert hasattr(mod.SimpleClient, "connect")
        sig = inspect.signature(mod.SimpleClient.connect)
        params = list(sig.parameters.keys())
        assert "url" in params
        assert "headers" in params
        assert "auth" in params
        assert "transports" in params
        assert "namespace" in params
        assert "socketio_path" in params
        assert "wait_timeout" in params

    def test_sid_property(self) -> None:
        assert hasattr(mod.SimpleClient, "sid")

    def test_transport_property(self) -> None:
        assert hasattr(mod.SimpleClient, "transport")

    def test_emit_method(self) -> None:
        assert hasattr(mod.SimpleClient, "emit")
        sig = inspect.signature(mod.SimpleClient.emit)
        params = list(sig.parameters.keys())
        assert "event" in params
        assert "data" in params

    def test_call_method(self) -> None:
        assert hasattr(mod.SimpleClient, "call")
        sig = inspect.signature(mod.SimpleClient.call)
        params = list(sig.parameters.keys())
        assert "event" in params
        assert "data" in params
        assert "timeout" in params

    def test_receive_method(self) -> None:
        assert hasattr(mod.SimpleClient, "receive")
        sig = inspect.signature(mod.SimpleClient.receive)
        params = list(sig.parameters.keys())
        assert "timeout" in params

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.SimpleClient, "disconnect")
        assert callable(mod.SimpleClient.disconnect)

    def test_enter_method(self) -> None:
        assert hasattr(mod.SimpleClient, "__enter__")
        assert callable(mod.SimpleClient.__enter__)

    def test_exit_method(self) -> None:
        assert hasattr(mod.SimpleClient, "__exit__")
        assert callable(mod.SimpleClient.__exit__)

    def test_connected_event_attribute(self) -> None:
        client = mod.SimpleClient()
        assert hasattr(client, "connected_event")
        assert_type(client.connected_event, Event)
        assert isinstance(client.connected_event, Event)

    def test_input_buffer_attribute(self) -> None:
        client = mod.SimpleClient()
        assert hasattr(client, "input_buffer")
        assert isinstance(client.input_buffer, list)
