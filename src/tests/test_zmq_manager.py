"""Tests for socketio.zmq_manager stub types."""

from __future__ import annotations

import inspect

import socketio.pubsub_manager as pubsub_mod
import socketio.zmq_manager as mod


class TestZmqManager:
    """Test ZmqManager class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "ZmqManager")
        assert inspect.isclass(mod.ZmqManager)

    def test_inherits_pubsub_manager(self) -> None:
        assert issubclass(mod.ZmqManager, pubsub_mod.PubSubManager)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.ZmqManager.__init__)
        params = list(sig.parameters.keys())
        assert params == ["self", "url", "channel", "write_only", "logger", "json"]

    def test_name_attribute(self) -> None:
        assert hasattr(mod.ZmqManager, "name")

    def test_url_in_init(self) -> None:
        sig = inspect.signature(mod.ZmqManager.__init__)
        params = list(sig.parameters.keys())
        assert "url" in params

    def test_channel_in_init(self) -> None:
        sig = inspect.signature(mod.ZmqManager.__init__)
        params = list(sig.parameters.keys())
        assert "channel" in params

    def test_zmq_listen_method(self) -> None:
        assert hasattr(mod.ZmqManager, "zmq_listen")
        assert callable(mod.ZmqManager.zmq_listen)
