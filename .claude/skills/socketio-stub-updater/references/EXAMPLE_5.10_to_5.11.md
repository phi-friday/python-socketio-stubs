# Example: Updating Stubs from v5.10.0 to v5.11.0

This document shows a complete example of updating python-socketio-stubs based on actual changes between python-socketio versions v5.10.0 and v5.11.0.

## 1. Detect Changes

### Setup Repository

```bash
# Clone python-socketio source if not already present
if [ ! -d /tmp/python-socketio-source ]; then
    git clone --depth=100 https://github.com/miguelgrinberg/python-socketio.git /tmp/python-socketio-source
fi
cd /tmp/python-socketio-source
git fetch --tags
```

### Generate Diff

```bash
# View public API changes
git diff v5.10.0..v5.11.0 -- src/socketio/__init__.py

# Check specific module changes
git diff v5.10.0..v5.11.0 -- src/socketio/server.py | head -100
git diff v5.10.0..v5.11.0 -- src/socketio/async_server.py | grep -E "def (emit|send)" -A 10
```

### Key Changes Found:

**Public API (needs stub updates):**
- ✅ `__init__.py`: New exports for middleware classes
- ✅ `Server.emit`: new `namespace` parameter type refinement
- ✅ `AsyncServer`: new `disconnect` method signature

**Internal/formatting (can skip):**
- Import statement reorganization
- Docstring updates
- Code formatting changes

## 2. Update __init__.pyi

Add new exports to `src/socketio-stubs/__init__.pyi`:

```python
# Before (v5.10.0) - middleware not exported
from socketio.server import Server as Server
from socketio.async_server import AsyncServer as AsyncServer
# ... other imports

# After (v5.11.0) - add middleware exports
from socketio.middleware import WSGIApp as WSGIApp
from socketio.asgi import ASGIApp as ASGIApp
from socketio.server import Server as Server
from socketio.async_server import AsyncServer as AsyncServer
# ... other imports

# Also update __all__
__all__ = [
    # ... existing exports
    "WSGIApp",
    "ASGIApp",
    # ... other exports
]
```

**Verification:**
```bash
cd /tmp/python-socketio-source
git diff v5.10.0..v5.11.0 -- src/socketio/__init__.py | grep "WSGIApp\|ASGIApp"
```

Output shows these were added to imports in v5.11.0.

## 3. Update server.pyi

Refine parameter type for `Server.emit`:

**Verification:**
```bash
cd /tmp/python-socketio-source

# Check v5.10.0 signature
git show v5.10.0:src/socketio/server.py | grep "def emit" -A 10
# Output: def emit(self, event, data=None, to=None, room=None,
#                  skip_sid=None, namespace=None, callback=None):

# Check v5.11.0 signature  
git show v5.11.0:src/socketio/server.py | grep "def emit" -A 10
# Output: def emit(self, event, data=None, to=None, room=None,
#                  skip_sid=None, namespace='/', callback=None):
```

**Stub Update:**
```python
# Necessary imports at top of file (absolute paths)
from typing import Any
from collections.abc import Callable

from socketio._types import Namespace
from socketio.base_server import BaseServer

# Before (v5.10.0 stub)
class Server(BaseServer):
    def emit(
        self,
        event: str,
        data: Any = ...,
        to: str | None = ...,
        room: str | None = ...,
        skip_sid: str | None = ...,
        namespace: Namespace | None = ...,  # CHANGE THIS
        callback: Callable[..., Any] | None = ...,
    ) -> None: ...

# After (v5.11.0 stub)
class Server(BaseServer):
    def emit(
        self,
        event: str,
        data: Any = ...,
        to: str | None = ...,
        room: str | None = ...,
        skip_sid: str | None = ...,
        namespace: Namespace = ...,  # default is '/' not None
        callback: Callable[..., Any] | None = ...,
    ) -> None: ...
```

## 4. Update async_server.pyi

Add new `disconnect` method signature:

**Verification:**
```bash
cd /tmp/python-socketio-source

# Check the diff
git diff v5.10.0..v5.11.0 -- src/socketio/async_server.py | grep -E "def disconnect" -A 10

# Output shows:
# +    async def disconnect(self, sid, namespace='/', ignore_queue=False):
```

**Stub Update:**
```python
# Necessary imports at top of file (absolute paths)
from socketio._types import Namespace
from socketio.base_server import BaseServer

# Before (v5.10.0 stub) - method didn't have ignore_queue parameter
class AsyncServer(BaseServer):
    async def disconnect(
        self,
        sid: str,
        namespace: Namespace = ...,
    ) -> None: ...  # ADD ignore_queue PARAMETER

# After (v5.11.0 stub)
class AsyncServer(BaseServer):
    async def disconnect(
        self,
        sid: str,
        namespace: Namespace = ...,
        ignore_queue: bool = ...,
    ) -> None: ...
```

## 5. Validate Changes

After updating all stubs, run full validation:

```bash
# Navigate back to stub repository
cd /home/phi/git/python/repo/python-socketio-stubs

# Format and lint
uv run poe lint

# Type check with both checkers
uv run poe pyright
uv run poe mypy

# Run affected tests
uv run pytest src/tests/test_server.py -v
uv run pytest src/tests/test_async_server.py -v
uv run pytest src/tests/ -v  # All tests
```

## 6. Update Tests

Update signature tests to match new signatures:

```python
# In src/tests/test_server.py
class TestServer:
    def test_emit_signature(self) -> None:
        sig = inspect.signature(mod.Server.emit)
        params = list(sig.parameters.keys())
        # namespace parameter should have default value
        assert sig.parameters["namespace"].default != inspect.Parameter.empty

# In src/tests/test_async_server.py
class TestAsyncServer:
    def test_disconnect_signature(self) -> None:
        sig = inspect.signature(mod.AsyncServer.disconnect)
        params = list(sig.parameters.keys())
        # ignore_queue should be in parameters
        assert "ignore_queue" in params
        assert params == ["self", "sid", "namespace", "ignore_queue"]
```

## Summary Checklist

| Module | Change | Status |
|--------|--------|--------|
| `__init__.pyi` | Add `WSGIApp`, `ASGIApp` exports | ☐ |
| `server.pyi` | Refine `namespace` parameter type in `emit` | ☐ |
| `async_server.pyi` | Add `ignore_queue` parameter to `disconnect` | ☐ |
| Tests | Update signature tests | ☐ |
| Validate | `uv run poe lint && uv run poe pyright && uv run poe mypy` | ☐ |

## Complete Workflow Summary

```bash
# 1. Check versions
uv run python -c "import socketio; print(socketio.__version__)"  # Current: v5.10.0
curl -s https://pypi.org/pypi/python-socketio/json | uv run python -c "import sys, json; print(json.load(sys.stdin)['info']['version'])"  # Latest: v5.11.0

# 2. Clone and analyze
if [ ! -d /tmp/python-socketio-source ]; then
    git clone --depth=100 https://github.com/miguelgrinberg/python-socketio.git /tmp/python-socketio-source
fi
cd /tmp/python-socketio-source
git fetch --tags
git diff v5.10.0..v5.11.0 -- src/socketio/__init__.py src/socketio/server.py src/socketio/async_server.py > /tmp/socketio-v5.10.0-to-v5.11.0.diff

# 3. Review changes
less /tmp/socketio-v5.10.0-to-v5.11.0.diff

# 4. Update stubs (manual editing in VS Code)
# - Edit src/socketio-stubs/__init__.pyi
# - Edit src/socketio-stubs/server.pyi
# - Edit src/socketio-stubs/async_server.pyi
# - Edit src/tests/test_server.py
# - Edit src/tests/test_async_server.py

# 5. Validate
cd /home/phi/git/python/repo/python-socketio-stubs
uv run poe lint && uv run poe pyright && uv run poe mypy && uv run pytest src/tests/ -v
```
