"""Tests for socketio.exceptions stub types."""

from __future__ import annotations

import inspect

import socketio.exceptions as mod


class TestSocketIOError:
    """Test SocketIOError type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "SocketIOError")
        assert inspect.isclass(mod.SocketIOError)

    def test_inherits_exception(self) -> None:
        assert issubclass(mod.SocketIOError, Exception)


class TestConnectionError:
    """Test ConnectionError type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "ConnectionError")
        assert inspect.isclass(mod.ConnectionError)

    def test_inherits_socketio_error(self) -> None:
        assert issubclass(mod.ConnectionError, mod.SocketIOError)


class TestConnectionRefusedError:
    """Test ConnectionRefusedError type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "ConnectionRefusedError")
        assert inspect.isclass(mod.ConnectionRefusedError)

    def test_inherits_connection_error(self) -> None:
        assert issubclass(mod.ConnectionRefusedError, mod.ConnectionError)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.ConnectionRefusedError.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "args" in params

    def test_error_args_attribute(self) -> None:
        err = mod.ConnectionRefusedError("test", {"reason": "refused"})
        assert hasattr(err, "error_args")


class TestTimeoutError:
    """Test TimeoutError type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "TimeoutError")
        assert inspect.isclass(mod.TimeoutError)

    def test_inherits_socketio_error(self) -> None:
        assert issubclass(mod.TimeoutError, mod.SocketIOError)


class TestBadNamespaceError:
    """Test BadNamespaceError type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "BadNamespaceError")
        assert inspect.isclass(mod.BadNamespaceError)

    def test_inherits_socketio_error(self) -> None:
        assert issubclass(mod.BadNamespaceError, mod.SocketIOError)


class TestDisconnectedError:
    """Test DisconnectedError type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "DisconnectedError")
        assert inspect.isclass(mod.DisconnectedError)

    def test_inherits_socketio_error(self) -> None:
        assert issubclass(mod.DisconnectedError, mod.SocketIOError)
