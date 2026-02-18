
# Test project using Selenium and pytest

Running `pytest` starts a local server serving the test web page at app/static/index.html and executes test cases from the tests/ directory.

## Requirements
- Python 3.10+
- Git
- Google Chrome, Mozilla Firefox, or Microsoft Edge (for browser automation)

## Quick setup (Windows PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m pytest -q
```

## Quick setup (macOS / Linux)

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m pytest -q
```

## Run tests with a different browser

```
python -m pytest -q --browser=firefox
python -m pytest -q --browser=edge
```

## Notes
- The server automatically starts on port 8000 via a fixture in [tests/conftest.py](tests/conftest.py).
- If port 8000 is already in use, tests may fail to start.
- Chrome is used by default, but you can specify Firefox or Edge with the `--browser` option.

## Files
- [tests/conftest.py](tests/conftest.py) — server auto-start and pytest configuration
- [requirements.txt](requirements.txt) — project dependencies
- [app/server.py](app/server.py) — standalone server script
- [pages/](pages/) — page object models
- [tests/](tests/) — test cases
- [app/static/index.html](app/static/index.html) — test web page
