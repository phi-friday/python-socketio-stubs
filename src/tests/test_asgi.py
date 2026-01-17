"""Tests for socketio.asgi stub types."""

from __future__ import annotations

import inspect

import engineio

import socketio.asgi as mod


class TestASGIApp:
    """Test ASGIApp class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "ASGIApp")
        assert inspect.isclass(mod.ASGIApp)

    def test_inherits_engineio_asgiapp(self) -> None:
        assert issubclass(mod.ASGIApp, engineio.ASGIApp)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.ASGIApp.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "socketio_server" in params
        assert "other_asgi_app" in params
        assert "static_files" in params
        assert "socketio_path" in params
        assert "on_startup" in params
        assert "on_shutdown" in params
