"""Tests for socketio.middleware stub types."""

from __future__ import annotations

import inspect

import engineio

import socketio.middleware as mod


class TestWSGIApp:
    """Test WSGIApp class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "WSGIApp")
        assert inspect.isclass(mod.WSGIApp)

    def test_inherits_engineio_wsgiapp(self) -> None:
        assert issubclass(mod.WSGIApp, engineio.WSGIApp)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.WSGIApp.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "socketio_app" in params
        assert "wsgi_app" in params
        assert "static_files" in params
        assert "socketio_path" in params


class TestMiddleware:
    """Test Middleware class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "Middleware")
        assert inspect.isclass(mod.Middleware)

    def test_inherits_wsgiapp(self) -> None:
        assert issubclass(mod.Middleware, mod.WSGIApp)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.Middleware.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "socketio_app" in params
        assert "wsgi_app" in params
        assert "socketio_path" in params
