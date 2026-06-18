"""Tests for socketio.redis_manager stub types."""

from __future__ import annotations

import inspect

import socketio.pubsub_manager as pubsub_mod
import socketio.redis_manager as mod


class TestRemovedLogger:
    """Test removed logger module attribute."""

    def test_not_exported(self) -> None:
        assert not hasattr(mod, "logger")


class TestParseRedisSentinelUrl:
    """Test parse_redis_sentinel_url function."""

    def test_exists(self) -> None:
        assert hasattr(mod, "parse_redis_sentinel_url")
        assert callable(mod.parse_redis_sentinel_url)

    def test_signature(self) -> None:
        sig = inspect.signature(mod.parse_redis_sentinel_url)
        params = list(sig.parameters.keys())
        assert params == ["url"]


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
        assert params == [
            "self",
            "url",
            "channel",
            "write_only",
            "logger",
            "json",
            "redis_options",
        ]

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
