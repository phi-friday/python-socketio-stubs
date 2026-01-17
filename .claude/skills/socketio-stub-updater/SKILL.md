---
name: socketio-stub-updater
description: >
  Detects changes between python-socketio versions by comparing git diffs, analyzes API changes 
  (new/modified/removed functions, classes, parameters), and updates corresponding .pyi stub files.
  Use when python-socketio releases a new version and stubs need to be synchronized, or when the user 
  mentions "update stubs", "socketio upgrade", "sync stubs with socketio", or "check socketio changes".
license: MIT
compatibility: Requires git, uv, and Python 3.11+. Internet access needed to fetch python-socketio releases.
allowed-tools: Bash(git:*) Bash(uv:*) Read Write
---

# Python-SocketIO Stub Updater

This skill helps maintain type stubs for python-socketio by detecting API changes between versions and updating `.pyi` files accordingly.

## Workflow Overview

```
1. Detect Version Change  →  2. Generate Diff  →  3. Analyze Changes  →  4. Update Stubs  →  5. Validate
```

## Step 1: Check Current and Latest Versions

First, determine what versions we're working with:

```bash
# Check currently stubbed version (from pyproject.toml or installed)
uv run python -c "import socketio; print(socketio.__version__)"

# Check latest available version from PyPI
curl -s https://pypi.org/pypi/python-socketio/json | uv run python -c "import sys, json; print(json.load(sys.stdin)['info']['version'])"
```

## Step 2: Clone Python-SocketIO and Generate Diff

Clone the python-socketio repository and generate a diff between versions:

```bash
# Clone python-socketio to a temp directory (skip if already exists)
if [ ! -d /tmp/python-socketio-source ]; then
    git clone --depth=100 https://github.com/miguelgrinberg/python-socketio.git /tmp/python-socketio-source
fi

# Navigate to the repository and update tags
cd /tmp/python-socketio-source
git fetch --tags

# List available tags
git tag --sort=-v:refname | head -20

# Generate diff between two versions (e.g., v5.10.0 to v5.11.0)
git diff <OLD_TAG>..<NEW_TAG> -- src/socketio/*.py
```

## Step 3: Analyze API Changes

Run the analysis script to identify what changed:

```bash
uv run python .github/skills/socketio-stub-updater/scripts/analyze_changes.py \
    --old-version <OLD_TAG> \
    --new-version <NEW_TAG> \
    --socketio-path /tmp/python-socketio-source
```

The script will output:
- **New exports**: Functions/classes added to `__all__` or public API
- **Removed exports**: Functions/classes removed from public API  
- **Signature changes**: Parameters added, removed, or type-changed
- **New modules**: Entirely new `.py` files
- **Deprecated items**: Functions/classes marked as deprecated

### Manual Diff Analysis

If the script is unavailable, manually analyze the diff:

```bash
# Navigate to python-socketio source (assumes Step 2 completed)
cd /tmp/python-socketio-source

# Focus on public API changes
git diff <OLD_TAG>..<NEW_TAG> -- src/socketio/__init__.py

# Check specific module changes
git diff <OLD_TAG>..<NEW_TAG> -- src/socketio/server.py
git diff <OLD_TAG>..<NEW_TAG> -- src/socketio/async_server.py
git diff <OLD_TAG>..<NEW_TAG> -- src/socketio/client.py

# Look for signature changes (def lines)
git diff <OLD_TAG>..<NEW_TAG> -- 'src/socketio/*.py' | grep -E '^\+.*def |^\-.*def '
```

## Step 4: Update Stub Files

For each identified change, update the corresponding `.pyi` file:

### Adding New Function

```pythonsocketio
# In src/joblib-stubs/<module>.pyi
def new_function(
    param1: str,
    param2: int = ...,
    *,
    keyword_only: bool = ...,
) -> ReturnType: ...
```

### Adding New Class

```python
class NewClass:
    attr: ClassVar[int]
    
    def __init__(self, param: str) -> None: ...
    def method(self, arg: int) -> str: ...
```

### Modifying Signatures

When a function signature changes:
1. Check the new signature in joblib source
2. Update parameter types and return type
3. Add overloads if the function has multiple valid signatures

```python
@overload
def func(x: int) -> int: ...
@overload  
def func(x: str) -> str: ...
def func(x: int | str) -> int | str: ...
```

### Removing Deprecated Items

If something is removed:
1. Check if it's in stubs
2. Remove from `.pyi` file
3. Remove from `__init__.pyi` re-exports if applicable

## Step 5: Validate Changes

After updating stubs, run full validation:

```bash
cd /path/to/python-socketio-stubs

# Format and lint
uv run poe lint

# Type check with both checkers
uv run poe pyright
uv run poe mypy

# Run affected tests
uv run pytest src/tests/test_<module>.py -v
```

## Example: Complete Update Flow

### Scenario: Update from python-socketio v5.10.0 to v5.11.0

```bash
# 1. Setup - Clone python-socketio repository
if [ ! -d /tmp/python-socketio-source ]; then
    git clone --depth=100 https://github.com/miguelgrinberg/python-socketio.git /tmp/python-socketio-source
fi
cd /tmp/python-socketio-source
git fetch --tags

# 2. Generate diff
git diff v5.10.0..v5.11.0 -- 'src/socketio/*.py' > /tmp/socketio-diff.patch

# 3. Review public API changes
git diff v5.10.0..v5.11.0 -- src/socketio/__init__.py
git diff v5.10.0..v5.11.0 -- src/socketio/server.py | head -100

# 4. Check new function signatures
git show v5.11.0:src/socketio/server.py | grep -A 20 "def new_function"

# 5. Update stub - Navigate back to stub repository
cd /home/phi/git/python/repo/python-socketio-stubs
# Edit src/socketio-stubs/server.pyi to add new_function

# 6. Validate
uv run poe lint && uv run poe pyright && uv run poe mypy
```

## Change Categories & Actions

| Change Type | Detection | Action |
|-------------|-----------|--------|
| New public function | `+def ` in `__all__` or module | Add to `.pyi` with types |
| New class | `+class ` | Add class stub with methods |
| New parameter | `def func(..., new_param` | Add to stub signature |
| Removed parameter | `-def func(..., old_param` | Remove from stub |
| Type change | Parameter/return type differs | Update type annotation |
| New module | New `.py` file | Create new `.pyi` file |
| Removed function | `-def ` or removed from `__all__` | Remove from stub |
| Deprecated | `@deprecated` or warnings | Add deprecation notice |

## Tips

1. **Always verify runtime behavior first**:
   ```bash
   uv run python -c "import inspect; from socketio import X; print(inspect.signature(X))"
   ```

2. **Check if default values matter for types**:
   ```python
   # If default is None, the type should include None
   def func(param: str | None = ...) -> str: ...
   ```

3. **Handle `*args` and `**kwargs` properly**:
   ```python
   def func(*args: Any, **kwargs: Any) -> Result: ...
   ```

4. **Use `_types.pyi` for complex internal types**

5. **Write tests for new additions** following the patterns in `AGENTS.md`

## Reference Files

- [AGENTS.md](../../../AGENTS.md) - Detailed stub writing conventions
- [analyze_changes.py](scripts/analyze_changes.py) - Automated change analysis script
