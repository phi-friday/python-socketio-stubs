"""Tests for socketio.base_server stub types."""

from __future__ import annotations

import inspect
import logging
from typing import assert_type

import socketio.base_server as mod


class TestDefaultLogger:
    """Test default_logger module attribute."""

    def test_exists(self) -> None:
        assert hasattr(mod, "default_logger")

    def test_type(self) -> None:
        assert_type(mod.default_logger, logging.Logger)
        assert isinstance(mod.default_logger, logging.Logger)


class TestBaseServer:
    """Test BaseServer class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "BaseServer")
        assert inspect.isclass(mod.BaseServer)

    def test_reserved_events_class_var(self) -> None:
        assert hasattr(mod.BaseServer, "reserved_events")

    def test_reason_class_var(self) -> None:
        assert hasattr(mod.BaseServer, "reason")

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.BaseServer.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "client_manager" in params
        assert "logger" in params
        assert "serializer" in params
        assert "json" in params
        assert "async_handlers" in params
        assert "always_connect" in params
        assert "namespaces" in params

    def test_is_asyncio_based_method(self) -> None:
        assert hasattr(mod.BaseServer, "is_asyncio_based")
        assert callable(mod.BaseServer.is_asyncio_based)

    def test_on_method(self) -> None:
        assert hasattr(mod.BaseServer, "on")
        assert callable(mod.BaseServer.on)

    def test_event_method(self) -> None:
        assert hasattr(mod.BaseServer, "event")
        assert callable(mod.BaseServer.event)

    def test_register_namespace_method(self) -> None:
        assert hasattr(mod.BaseServer, "register_namespace")
        assert callable(mod.BaseServer.register_namespace)

    def test_rooms_method(self) -> None:
        assert hasattr(mod.BaseServer, "rooms")
        assert callable(mod.BaseServer.rooms)

    def test_transport_method(self) -> None:
        assert hasattr(mod.BaseServer, "transport")
        assert callable(mod.BaseServer.transport)

    def test_get_environ_method(self) -> None:
        assert hasattr(mod.BaseServer, "get_environ")
        assert callable(mod.BaseServer.get_environ)
