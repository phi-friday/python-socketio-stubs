"""Tests for socketio.base_client stub types."""

from __future__ import annotations

import inspect
import logging
from typing import assert_type

import socketio.base_client as mod


class TestDefaultLogger:
    """Test default_logger module attribute."""

    def test_exists(self) -> None:
        assert hasattr(mod, "default_logger")

    def test_type(self) -> None:
        assert_type(mod.default_logger, logging.Logger)
        assert isinstance(mod.default_logger, logging.Logger)


class TestReconnectingClients:
    """Test reconnecting_clients module attribute."""

    def test_exists(self) -> None:
        assert hasattr(mod, "reconnecting_clients")

    def test_type(self) -> None:
        assert isinstance(mod.reconnecting_clients, list)


class TestSignalHandler:
    """Test signal_handler function."""

    def test_exists(self) -> None:
        assert hasattr(mod, "signal_handler")
        assert callable(mod.signal_handler)


class TestOriginalSignalHandler:
    """Test original_signal_handler module attribute."""

    def test_exists(self) -> None:
        assert hasattr(mod, "original_signal_handler")


class TestBaseClient:
    """Test BaseClient class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "BaseClient")
        assert inspect.isclass(mod.BaseClient)

    def test_reserved_events_class_var(self) -> None:
        assert hasattr(mod.BaseClient, "reserved_events")

    def test_reason_class_var(self) -> None:
        assert hasattr(mod.BaseClient, "reason")

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.BaseClient.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "reconnection" in params
        assert "reconnection_attempts" in params
        assert "reconnection_delay" in params
        assert "reconnection_delay_max" in params
        assert "randomization_factor" in params
        assert "logger" in params
        assert "serializer" in params
        assert "json" in params
        assert "handle_sigint" in params

    def test_is_asyncio_based_method(self) -> None:
        assert hasattr(mod.BaseClient, "is_asyncio_based")
        assert callable(mod.BaseClient.is_asyncio_based)

    def test_on_method(self) -> None:
        assert hasattr(mod.BaseClient, "on")
        assert callable(mod.BaseClient.on)

    def test_event_method(self) -> None:
        assert hasattr(mod.BaseClient, "event")
        assert callable(mod.BaseClient.event)

    def test_register_namespace_method(self) -> None:
        assert hasattr(mod.BaseClient, "register_namespace")
        assert callable(mod.BaseClient.register_namespace)

    def test_get_sid_method(self) -> None:
        assert hasattr(mod.BaseClient, "get_sid")
        assert callable(mod.BaseClient.get_sid)

    def test_transport_method(self) -> None:
        assert hasattr(mod.BaseClient, "transport")
        assert callable(mod.BaseClient.transport)
