"""Tests for socketio.async_simple_client stub types."""

from __future__ import annotations

import asyncio
import inspect
from typing import assert_type

import socketio.async_client as async_client_mod
import socketio.async_simple_client as mod


class TestAsyncSimpleClient:
    """Test AsyncSimpleClient class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "AsyncSimpleClient")
        assert inspect.isclass(mod.AsyncSimpleClient)

    def test_client_class_class_var(self) -> None:
        assert hasattr(mod.AsyncSimpleClient, "client_class")
        assert mod.AsyncSimpleClient.client_class is async_client_mod.AsyncClient

    def test_init_accepts_any_args(self) -> None:
        sig = inspect.signature(mod.AsyncSimpleClient.__init__)
        params = list(sig.parameters.keys())
        # Exact match to catch stub/runtime mismatches
        assert params == ["self", "args", "kwargs"]

    def test_client_attribute_type(self) -> None:
        """Verify client attribute is AsyncClient | None, not Client | None."""
        client = mod.AsyncSimpleClient()
        assert hasattr(client, "client")
        # Should be None initially (before connect)
        assert_type(client.client, async_client_mod.AsyncClient | None)
        assert client.client is None

    def test_connect_method(self) -> None:
        assert hasattr(mod.AsyncSimpleClient, "connect")
        sig = inspect.signature(mod.AsyncSimpleClient.connect)
        params = list(sig.parameters.keys())
        # Exact match to catch stub/runtime mismatches
        assert params == [
            "self",
            "url",
            "headers",
            "auth",
            "transports",
            "namespace",
            "socketio_path",
            "wait_timeout",
        ]

    def test_sid_property(self) -> None:
        assert hasattr(mod.AsyncSimpleClient, "sid")

    def test_transport_property(self) -> None:
        assert hasattr(mod.AsyncSimpleClient, "transport")

    def test_emit_method(self) -> None:
        assert hasattr(mod.AsyncSimpleClient, "emit")
        sig = inspect.signature(mod.AsyncSimpleClient.emit)
        params = list(sig.parameters.keys())
        # Exact match to catch stub/runtime mismatches
        assert params == ["self", "event", "data"]

    def test_call_method(self) -> None:
        assert hasattr(mod.AsyncSimpleClient, "call")
        sig = inspect.signature(mod.AsyncSimpleClient.call)
        params = list(sig.parameters.keys())
        # Exact match to catch stub/runtime mismatches
        assert params == ["self", "event", "data", "timeout"]

    def test_receive_method(self) -> None:
        assert hasattr(mod.AsyncSimpleClient, "receive")
        sig = inspect.signature(mod.AsyncSimpleClient.receive)
        params = list(sig.parameters.keys())
        # Exact match to catch stub/runtime mismatches
        assert params == ["self", "timeout"]

    def test_disconnect_method(self) -> None:
        assert hasattr(mod.AsyncSimpleClient, "disconnect")
        assert callable(mod.AsyncSimpleClient.disconnect)

    def test_aenter_method(self) -> None:
        assert hasattr(mod.AsyncSimpleClient, "__aenter__")
        assert callable(mod.AsyncSimpleClient.__aenter__)

    def test_context_manager_exit_method(self) -> None:
        assert hasattr(mod.AsyncSimpleClient, "__aexit__")
        assert callable(mod.AsyncSimpleClient.__aexit__)

    def test_connected_event_attribute(self) -> None:
        client = mod.AsyncSimpleClient()
        assert hasattr(client, "connected_event")
        assert_type(client.connected_event, asyncio.Event)
        assert isinstance(client.connected_event, asyncio.Event)

    def test_input_buffer_attribute(self) -> None:
        client = mod.AsyncSimpleClient()
        assert hasattr(client, "input_buffer")
        assert isinstance(client.input_buffer, list)
