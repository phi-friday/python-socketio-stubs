"""Tests for socketio.async_redis_manager stub types."""

from __future__ import annotations

import inspect

import socketio.async_pubsub_manager as async_pubsub_mod
import socketio.async_redis_manager as mod


class TestParseRedisSentinelUrl:
    """Test parse_redis_sentinel_url function."""

    def test_exists(self) -> None:
        assert hasattr(mod, "parse_redis_sentinel_url")
        assert callable(mod.parse_redis_sentinel_url)

    def test_signature(self) -> None:
        sig = inspect.signature(mod.parse_redis_sentinel_url)
        params = list(sig.parameters.keys())
        assert "url" in params


class TestAsyncRedisManager:
    """Test AsyncRedisManager class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "AsyncRedisManager")
        assert inspect.isclass(mod.AsyncRedisManager)

    def test_inherits_async_pubsub_manager(self) -> None:
        assert issubclass(mod.AsyncRedisManager, async_pubsub_mod.AsyncPubSubManager)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.AsyncRedisManager.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "url" in params
        assert "channel" in params
        assert "write_only" in params
        assert "logger" in params
        assert "redis_options" in params

    def test_name_attribute(self) -> None:
        assert hasattr(mod.AsyncRedisManager, "name")

    def test_url_in_init(self) -> None:
        sig = inspect.signature(mod.AsyncRedisManager.__init__)
        params = list(sig.parameters.keys())
        assert "url" in params

    def test_redis_options_in_init(self) -> None:
        sig = inspect.signature(mod.AsyncRedisManager.__init__)
        params = list(sig.parameters.keys())
        assert "redis_options" in params
