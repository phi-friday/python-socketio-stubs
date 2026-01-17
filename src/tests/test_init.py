"""Tests for socketio.__init__ stub types (public API re-exports)."""

from __future__ import annotations

import socketio
import socketio.asgi
import socketio.async_aiopika_manager
import socketio.async_client
import socketio.async_manager
import socketio.async_namespace
import socketio.async_redis_manager
import socketio.async_server
import socketio.async_simple_client
import socketio.client
import socketio.kafka_manager
import socketio.kombu_manager
import socketio.manager
import socketio.middleware
import socketio.namespace
import socketio.pubsub_manager
import socketio.redis_manager
import socketio.server
import socketio.simple_client
import socketio.tornado
import socketio.zmq_manager


class TestPublicReexports:
    """Test that all public API is correctly re-exported."""

    def test_asgiapp(self) -> None:
        assert socketio.ASGIApp is socketio.asgi.ASGIApp

    def test_async_aiopika_manager(self) -> None:
        assert (
            socketio.AsyncAioPikaManager
            is socketio.async_aiopika_manager.AsyncAioPikaManager
        )

    def test_async_client(self) -> None:
        assert socketio.AsyncClient is socketio.async_client.AsyncClient

    def test_async_manager(self) -> None:
        assert socketio.AsyncManager is socketio.async_manager.AsyncManager

    def test_async_client_namespace(self) -> None:
        assert (
            socketio.AsyncClientNamespace
            is socketio.async_namespace.AsyncClientNamespace
        )

    def test_async_namespace(self) -> None:
        assert socketio.AsyncNamespace is socketio.async_namespace.AsyncNamespace

    def test_async_redis_manager(self) -> None:
        assert (
            socketio.AsyncRedisManager is socketio.async_redis_manager.AsyncRedisManager
        )

    def test_async_server(self) -> None:
        assert socketio.AsyncServer is socketio.async_server.AsyncServer

    def test_async_simple_client(self) -> None:
        assert (
            socketio.AsyncSimpleClient is socketio.async_simple_client.AsyncSimpleClient
        )

    def test_client(self) -> None:
        assert socketio.Client is socketio.client.Client

    def test_client_namespace(self) -> None:
        assert socketio.ClientNamespace is socketio.namespace.ClientNamespace

    def test_kafka_manager(self) -> None:
        assert socketio.KafkaManager is socketio.kafka_manager.KafkaManager

    def test_kombu_manager(self) -> None:
        assert socketio.KombuManager is socketio.kombu_manager.KombuManager

    def test_manager(self) -> None:
        assert socketio.Manager is socketio.manager.Manager

    def test_middleware(self) -> None:
        assert socketio.Middleware is socketio.middleware.Middleware

    def test_namespace(self) -> None:
        assert socketio.Namespace is socketio.namespace.Namespace

    def test_pubsub_manager(self) -> None:
        assert socketio.PubSubManager is socketio.pubsub_manager.PubSubManager

    def test_redis_manager(self) -> None:
        assert socketio.RedisManager is socketio.redis_manager.RedisManager

    def test_server(self) -> None:
        assert socketio.Server is socketio.server.Server

    def test_simple_client(self) -> None:
        assert socketio.SimpleClient is socketio.simple_client.SimpleClient

    def test_wsgiapp(self) -> None:
        assert socketio.WSGIApp is socketio.middleware.WSGIApp

    def test_zmq_manager(self) -> None:
        assert socketio.ZmqManager is socketio.zmq_manager.ZmqManager

    def test_get_tornado_handler(self) -> None:
        assert socketio.get_tornado_handler is socketio.tornado.get_tornado_handler


class TestAll:
    """Test __all__ exports."""

    def test_all_exists(self) -> None:
        assert hasattr(socketio, "__all__")

    def test_all_contains_expected(self) -> None:
        expected = [
            "ASGIApp",
            "AsyncAioPikaManager",
            "AsyncClient",
            "AsyncClientNamespace",
            "AsyncManager",
            "AsyncNamespace",
            "AsyncRedisManager",
            "AsyncServer",
            "AsyncSimpleClient",
            "Client",
            "ClientNamespace",
            "KafkaManager",
            "KombuManager",
            "Manager",
            "Middleware",
            "Namespace",
            "PubSubManager",
            "RedisManager",
            "Server",
            "SimpleClient",
            "WSGIApp",
            "ZmqManager",
            "get_tornado_handler",
        ]
        for name in expected:
            assert name in socketio.__all__, f"{name} not in __all__"
