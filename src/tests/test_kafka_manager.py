"""Tests for socketio.kafka_manager stub types."""

from __future__ import annotations

import inspect
import logging
from typing import assert_type

import socketio.kafka_manager as mod
import socketio.pubsub_manager as pubsub_mod


class TestLogger:
    """Test logger module attribute."""

    def test_exists(self) -> None:
        assert hasattr(mod, "logger")

    def test_type(self) -> None:
        assert_type(mod.logger, logging.Logger)
        assert isinstance(mod.logger, logging.Logger)


class TestKafkaManager:
    """Test KafkaManager class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "KafkaManager")
        assert inspect.isclass(mod.KafkaManager)

    def test_inherits_pubsub_manager(self) -> None:
        assert issubclass(mod.KafkaManager, pubsub_mod.PubSubManager)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.KafkaManager.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "url" in params
        assert "channel" in params
        assert "write_only" in params

    def test_name_attribute(self) -> None:
        assert hasattr(mod.KafkaManager, "name")

    def test_url_in_init(self) -> None:
        sig = inspect.signature(mod.KafkaManager.__init__)
        params = list(sig.parameters.keys())
        assert "url" in params
