"""Tests for socketio.base_namespace stub types."""

from __future__ import annotations

import inspect
from typing import assert_type

import socketio.base_namespace as mod


class TestBaseNamespace:
    """Test BaseNamespace class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "BaseNamespace")
        assert inspect.isclass(mod.BaseNamespace)

    def test_init_signature(self) -> None:
        sig = inspect.signature(mod.BaseNamespace.__init__)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "namespace" in params

    def test_namespace_attribute(self) -> None:
        ns = mod.BaseNamespace("/test")
        assert hasattr(ns, "namespace")
        assert_type(ns.namespace, str)
        assert isinstance(ns.namespace, str)

    def test_is_asyncio_based_method(self) -> None:
        ns = mod.BaseNamespace()
        assert hasattr(ns, "is_asyncio_based")
        assert callable(ns.is_asyncio_based)


class TestBaseServerNamespace:
    """Test BaseServerNamespace class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "BaseServerNamespace")
        assert inspect.isclass(mod.BaseServerNamespace)

    def test_inherits_base_namespace(self) -> None:
        assert issubclass(mod.BaseServerNamespace, mod.BaseNamespace)

    def test_rooms_method(self) -> None:
        assert hasattr(mod.BaseServerNamespace, "rooms")

    def test_set_server_method(self) -> None:
        assert hasattr(mod.BaseServerNamespace, "_set_server")


class TestBaseClientNamespace:
    """Test BaseClientNamespace class type hints."""

    def test_exists(self) -> None:
        assert hasattr(mod, "BaseClientNamespace")
        assert inspect.isclass(mod.BaseClientNamespace)

    def test_inherits_base_namespace(self) -> None:
        assert issubclass(mod.BaseClientNamespace, mod.BaseNamespace)

    def test_set_client_method(self) -> None:
        assert hasattr(mod.BaseClientNamespace, "_set_client")
