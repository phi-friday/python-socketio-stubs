"""Tests for socketio.async_aiopika_manager stub types."""

from __future__ import annotations

import inspect

import socketio.async_aiopika_manager as mod
import socketio.async_pubsub_manager as async_pubsub_mod


class TestAsyncAioPikaManager:
    """Test AsyncAioPikaManager class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "AsyncAioPikaManager")
        assert inspect.isclass(mod.AsyncAioPikaManager)

    def test_inherits_async_pubsub_manager(self) -> None:
        assert issubclass(mod.AsyncAioPikaManager, async_pubsub_mod.AsyncPubSubManager)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.AsyncAioPikaManager.__init__)
        params = list(sig.parameters.keys())
        assert params == ["self", "url", "channel", "write_only", "logger", "json"]

    def test_name_attribute(self) -> None:
        assert hasattr(mod.AsyncAioPikaManager, "name")

    def test_url_in_init(self) -> None:
        sig = inspect.signature(mod.AsyncAioPikaManager.__init__)
        params = list(sig.parameters.keys())
        assert "url" in params
