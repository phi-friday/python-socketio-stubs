"""Tests for socketio.kombu_manager stub types."""

from __future__ import annotations

import inspect

import socketio.kombu_manager as mod
import socketio.pubsub_manager as pubsub_mod


class TestKombuManager:
    """Test KombuManager class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "KombuManager")
        assert inspect.isclass(mod.KombuManager)

    def test_inherits_pubsub_manager(self) -> None:
        assert issubclass(mod.KombuManager, pubsub_mod.PubSubManager)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.KombuManager.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "url" in params
        assert "channel" in params
        assert "write_only" in params
        assert "logger" in params
        assert "connection_options" in params
        assert "exchange_options" in params
        assert "queue_options" in params
        assert "producer_options" in params

    def test_name_attribute(self) -> None:
        assert hasattr(mod.KombuManager, "name")

    def test_url_in_init(self) -> None:
        sig = inspect.signature(mod.KombuManager.__init__)
        params = list(sig.parameters.keys())
        assert "url" in params

    def test_connection_options_in_init(self) -> None:
        sig = inspect.signature(mod.KombuManager.__init__)
        params = list(sig.parameters.keys())
        assert "connection_options" in params

    def test_exchange_options_in_init(self) -> None:
        sig = inspect.signature(mod.KombuManager.__init__)
        params = list(sig.parameters.keys())
        assert "exchange_options" in params

    def test_queue_options_in_init(self) -> None:
        sig = inspect.signature(mod.KombuManager.__init__)
        params = list(sig.parameters.keys())
        assert "queue_options" in params

    def test_producer_options_in_init(self) -> None:
        sig = inspect.signature(mod.KombuManager.__init__)
        params = list(sig.parameters.keys())
        assert "producer_options" in params

    def test_initialize_method(self) -> None:
        assert hasattr(mod.KombuManager, "initialize")
        assert callable(mod.KombuManager.initialize)
