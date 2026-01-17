"""Tests for socketio.redis_manager stub types."""

from __future__ import annotations

import inspect
import logging
from typing import assert_type

import socketio.pubsub_manager as pubsub_mod
import socketio.redis_manager as mod


class TestLogger:
    """Test logger module attribute."""

    def test_exists(self) -> None:
        assert hasattr(mod, "logger")

    def test_type(self) -> None:
        assert_type(mod.logger, logging.Logger)
        assert isinstance(mod.logger, logging.Logger)


class TestParseRedisSentinelUrl:
    """Test parse_redis_sentinel_url function."""

    def test_exists(self) -> None:
        assert hasattr(mod, "parse_redis_sentinel_url")
        assert callable(mod.parse_redis_sentinel_url)

    def test_signature(self) -> None:
        sig = inspect.signature(mod.parse_redis_sentinel_url)
        params = list(sig.parameters.keys())
        assert "url" in params


class TestRedisManager:
    """Test RedisManager class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "RedisManager")
        assert inspect.isclass(mod.RedisManager)

    def test_inherits_pubsub_manager(self) -> None:
        assert issubclass(mod.RedisManager, pubsub_mod.PubSubManager)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.RedisManager.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "url" in params
        assert "channel" in params
        assert "write_only" in params
        assert "logger" in params
        assert "redis_options" in params

    def test_name_attribute(self) -> None:
        assert hasattr(mod.RedisManager, "name")

    def test_url_in_init(self) -> None:
        sig = inspect.signature(mod.RedisManager.__init__)
        params = list(sig.parameters.keys())
        assert "url" in params

    def test_redis_options_in_init(self) -> None:
        sig = inspect.signature(mod.RedisManager.__init__)
        params = list(sig.parameters.keys())
        assert "redis_options" in params

    def test_initialize_method(self) -> None:
        assert hasattr(mod.RedisManager, "initialize")
        assert callable(mod.RedisManager.initialize)
