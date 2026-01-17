# Stub Writing Reference

Detailed conventions for writing and maintaining python-socketio type stubs.

## Type Annotation Patterns

### Basic Patterns

```python
# Simple function
def func(param: str, count: int = ...) -> bool: ...

# Optional parameter (default is None)
def func(param: str | None = ...) -> str: ...

# With *args and **kwargs
def func(*args: Any, **kwargs: Any) -> Result: ...

# Keyword-only parameters
def func(pos_arg: int, *, keyword_only: str = ...) -> None: ...

# Positional-only parameters (Python 3.8+)
def func(pos_only: int, /, normal: str) -> None: ...
```

### Class Patterns

```python
from typing import ClassVar, Self

class MyClass:
    # Class variable
    class_attr: ClassVar[int]
    
    # Instance variable (declared without assignment)
    instance_attr: str
    
    def __init__(self, value: str) -> None: ...
    
    # Method returning same type
    def copy(self) -> Self: ...
    
    # Property
    @property
    def computed(self) -> int: ...
    
    # Setter
    @computed.setter
    def computed(self, value: int) -> None: ...
```

### Overloads

Use `@overload` when a function's return type depends on input types:

```python
from typing import overload

@overload
def process(data: str) -> str: ...
@overload
def process(data: bytes) -> bytes: ...
@overload
def process(data: list[int]) -> list[int]: ...
def process(data: str | bytes | list[int]) -> str | bytes | list[int]: ...
```

### Generic Types

```python
from typing import TypeVar, Generic
from collections.abc import Callable, Iterator

T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)

class Container(Generic[T]):
    def get(self) -> T: ...
    def set(self, value: T) -> None: ...

# Callable types
def apply(func: Callable[[int, str], bool], x: int, y: str) -> bool: ...

# With ParamSpec for decorators
from typing import ParamSpec, Concatenate

P = ParamSpec("P")

def decorator(func: Callable[P, T]) -> Callable[P, T]: ...
```

## Module Organization

### `__init__.pyi` Pattern

```python
# Use absolute imports (not relative)
# Re-export with explicit `as` syntax
from socketio.module import (
    PublicClass as PublicClass,
    public_function as public_function,
)

# Define __all__ if the source does
__all__ = ["PublicClass", "public_function"]
```

**Real Example from `__init__.pyi`:**
```python
from socketio.async_client import AsyncClient
from socketio.async_server import AsyncServer
from socketio.client import Client
from socketio.server import Server
from socketio.exceptions import (
    ConnectionError,
    DisconnectedError,
    SocketIOError,
)

__all__ = [
    "AsyncClient",
    "AsyncServer",
    "Client",
    "Server",
    "ConnectionError",
    "DisconnectedError",
    "SocketIOError",
    # ... more exports
]
```

### Internal Types (`_types.pyi`)

Put complex internal types here. Other modules import from this using absolute paths:

```python
# In src/socketio-stubs/_types.pyi
from typing import Protocol, TypeAlias
from collections.abc import Callable

# Type aliases
HandlerType: TypeAlias = Callable[..., None]
Namespace: TypeAlias = str

# Protocols for duck typing
class EngineProtocol(Protocol):
    def send(self, data: str | bytes) -> None: ...
    def close(self) -> None: ...
```

**Usage in other modules:**
```python
# In src/socketio-stubs/server.pyi
from socketio._types import HandlerType, Namespace  # Absolute import

def on(event: str, handler: HandlerType, namespace: Namespace = ...) -> None: ...
```

## Python-SocketIO Specific Patterns

### Server/Client Classes

```python
# Necessary imports (absolute paths)
from collections.abc import Callable
from typing import Any, overload

from socketio._types import HandlerType, Namespace
from socketio.base_server import BaseServer

class Server(BaseServer):
    async_handlers: bool
    always_connect: bool
    namespaces: dict[str, Any]
    
    def __init__(
        self,
        client_manager: Any | None = ...,
        logger: bool = ...,
        json: Any | None = ...,
        async_handlers: bool = ...,
        always_connect: bool = ...,
        **kwargs: Any,
    ) -> None: ...
    
    # Event handler registration with overloads
    @overload
    def on(
        self,
        event: str,
        handler: None = ...,
        namespace: Namespace = ...,
    ) -> Callable[[HandlerType], HandlerType]: ...
    @overload
    def on(
        self,
        event: str,
        handler: HandlerType,
        namespace: Namespace = ...,
    ) -> HandlerType: ...
    
    def emit(
        self,
        event: str,
        data: Any = ...,
        to: str | None = ...,
        room: str | None = ...,
        skip_sid: str | None = ...,
        namespace: Namespace = ...,
        callback: Callable[..., Any] | None = ...,
    ) -> None: ...
```

### Namespaces

```python
# Necessary imports (absolute paths)
from collections.abc import Callable
from typing import Any

from socketio._types import HandlerType
from socketio.base_namespace import BaseServerNamespace

class Namespace(BaseServerNamespace):
    def __init__(self, namespace: str | None = ...) -> None: ...
    
    def trigger_event(self, event: str, *args: Any) -> Any: ...
    def emit(
        self,
        event: str,
        data: Any = ...,
        to: str | None = ...,
        room: str | None = ...,
        skip_sid: str | None = ...,
        callback: Callable[..., Any] | None = ...,
    ) -> None: ...
    def send(
        self,
        data: Any,
        to: str | None = ...,
        room: str | None = ...,
        skip_sid: str | None = ...,
        callback: Callable[..., Any] | None = ...,
    ) -> None: ...
```

## Common Type Imports

```python
# Standard imports
from __future__ import annotations

import os
from collections.abc import (
    Awaitable,
    Callable,
    Coroutine,
    Generator,
    Iterable,
    Iterator,
    Mapping,
    MutableMapping,
    Sequence,
)
from pathlib import Path
from typing import (
    Any,
    ClassVar,
    Final,
    Generic,
    Literal,
    NamedTuple,
    Protocol,
    Self,
    TypeAlias,
    overload,
)

# Use typing_extensions for ParamSpec, TypeVar (for compatibility)
from typing_extensions import ParamSpec, TypeVar

# Absolute imports from socketio modules
from socketio._types import CustomType  # Internal types
from socketio.module import SomeClass
```

**Real Example from `server.pyi`:**
```python
from collections.abc import Callable
from typing import Any, overload

from socketio._types import HandlerType, Namespace
from socketio.base_server import BaseServer
```
```

## Deprecation Handling

When something is deprecated but still present:

```python
from typing import deprecated
from warnings import deprecated  # Python 3.13+

@deprecated("Use new_function instead")
def old_function(x: int) -> int: ...
```

Or with a comment:

```python
# Deprecated since 1.4.0, use new_function instead
def old_function(x: int) -> int: ...
```

## Mapping Source to Stub

### Source Code
```python
def process_data(data, *, normalize=True, fill_value=0):
    """Process input data.
    
    Parameters
    ----------
    data : array-like
        Input data
    normalize : bool, default=True
        Whether to normalize
    fill_value : int or float, default=0
        Value for missing data
    """
    if normalize:
        data = data / data.max()
    return data
```

### Corresponding Stub
```python
from numpy.typing import ArrayLike, NDArray

def process_data(
    data: ArrayLike,
    *,
    normalize: bool = ...,
    fill_value: int | float = ...,
) -> NDArray[Any]: ...
```

## Testing Checklist

After updating stubs:

1. [ ] `uv run poe lint` - passes
2. [ ] `uv run poe pyright` - passes
3. [ ] `uv run poe mypy` - passes
4. [ ] Tests added/updated for new APIs
5. [ ] `assert_type` checks match runtime behavior
