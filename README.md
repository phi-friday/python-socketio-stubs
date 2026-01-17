# python-socketio-stubs

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/python-socketio-stubs.svg)](https://badge.fury.io/py/python-socketio-stubs)
[![python version](https://img.shields.io/pypi/pyversions/python-socketio-stubs.svg)](#)

Type stubs for the [python-socketio](https://github.com/miguelgrinberg/python-socketio) library.

> [!NOTE]  
> This package provides type hints only and contains no runtime code.  
> For the actual runtime implementation, install [`python-socketio`](https://github.com/miguelgrinberg/python-socketio).

## Installation

```shell
pip install python-socketio-stubs
```

## Usage

Once installed, type checkers will automatically discover and use these stubs when analyzing code that uses `python-socketio`:

```python
from typing import Any, assert_type

import socketio

# Your type checker will now understand python-socketio's types
sio = socketio.Server()

@sio.event
def connect(sid: str, environ: dict[str, Any], auth: dict[str, Any] | None) -> None:
    session = sio.get_session(sid)
    assert_type(session, dict[str, Any])
```

## License

MIT - see [LICENSE](https://github.com/phi-friday/python-socketio-stubs/blob/main/LICENSE) for details.
