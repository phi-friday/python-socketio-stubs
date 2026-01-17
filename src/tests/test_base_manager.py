"""Tests for socketio.base_manager stub types."""

from __future__ import annotations

import inspect
import logging
from typing import assert_type

import socketio.base_manager as mod


class TestDefaultLogger:
    """Test default_logger module attribute."""

    def test_exists(self) -> None:
        assert hasattr(mod, "default_logger")

    def test_type(self) -> None:
        assert_type(mod.default_logger, logging.Logger)
        assert isinstance(mod.default_logger, logging.Logger)


class TestBaseManager:
    """Test BaseManager class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "BaseManager")
        assert inspect.isclass(mod.BaseManager)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.BaseManager.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params

    def test_set_server_method(self) -> None:
        assert hasattr(mod.BaseManager, "set_server")
        assert callable(mod.BaseManager.set_server)

    def test_initialize_method(self) -> None:
        assert hasattr(mod.BaseManager, "initialize")
        assert callable(mod.BaseManager.initialize)

    def test_get_namespaces_method(self) -> None:
        assert hasattr(mod.BaseManager, "get_namespaces")
        assert callable(mod.BaseManager.get_namespaces)

    def test_get_participants_method(self) -> None:
        assert hasattr(mod.BaseManager, "get_participants")
        assert callable(mod.BaseManager.get_participants)

    def test_connect_method(self) -> None:
        assert hasattr(mod.BaseManager, "connect")
        assert callable(mod.BaseManager.connect)

    def test_is_connected_method(self) -> None:
        assert hasattr(mod.BaseManager, "is_connected")
        assert callable(mod.BaseManager.is_connected)

    def test_sid_from_eio_sid_method(self) -> None:
        assert hasattr(mod.BaseManager, "sid_from_eio_sid")
        assert callable(mod.BaseManager.sid_from_eio_sid)

    def test_eio_sid_from_sid_method(self) -> None:
        assert hasattr(mod.BaseManager, "eio_sid_from_sid")
        assert callable(mod.BaseManager.eio_sid_from_sid)

    def test_pre_disconnect_method(self) -> None:
        assert hasattr(mod.BaseManager, "pre_disconnect")
        assert callable(mod.BaseManager.pre_disconnect)

    def test_basic_disconnect_method(self) -> None:
        assert hasattr(mod.BaseManager, "basic_disconnect")
        assert callable(mod.BaseManager.basic_disconnect)

    def test_basic_enter_room_method(self) -> None:
        assert hasattr(mod.BaseManager, "basic_enter_room")
        assert callable(mod.BaseManager.basic_enter_room)

    def test_basic_leave_room_method(self) -> None:
        assert hasattr(mod.BaseManager, "basic_leave_room")
        assert callable(mod.BaseManager.basic_leave_room)

    def test_basic_close_room_method(self) -> None:
        assert hasattr(mod.BaseManager, "basic_close_room")
        assert callable(mod.BaseManager.basic_close_room)

    def test_get_rooms_method(self) -> None:
        assert hasattr(mod.BaseManager, "get_rooms")
        assert callable(mod.BaseManager.get_rooms)

    def test_get_logger_method(self) -> None:
        assert hasattr(mod.BaseManager, "_get_logger")
        assert callable(mod.BaseManager._get_logger)  # noqa: SLF001
