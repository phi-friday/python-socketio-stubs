"""Tests for socketio.tornado stub types."""

from __future__ import annotations

import inspect

import socketio.tornado as mod


class TestGetTornadoHandler:
    """Test get_tornado_handler function type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "get_tornado_handler")
        assert callable(mod.get_tornado_handler)

    def test_signature(self) -> None:
        sig = inspect.signature(mod.get_tornado_handler)
        params = list(sig.parameters.keys())
        assert "socketio_server" in params
