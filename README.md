# Device Manager

A simple full-stack CRUD project for managing network devices. Designed as a QA automation candidate task, this project uses:

- **FastAPI** for the backend
- **Mocked MongoDB (mongomock)** for in-memory storage
- **Mocked Redis (fakeredis)** for caching
- **HTML + JS** frontend

---

## Features

- Add, view, update, and delete devices
- Search devices by name or IP address
- Device status indication with active/inactive states
- Visual status indicators (green/red light bulbs)
- Device data includes `name`, `ip_address`, `status`, `active` and `last_updated`
- Redis caching for `/api/devices` endpoint
- In-memory database and cache: no external services required

## Project Structure

```
backend/          # FastAPI app and logic
frontend/         # Simple HTML UI
tests/            # Pytest and Playwright test suites
requirements.txt  # Python dependencies
```

---

## Setup

### 1. Install dependencies

```bash
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
playwright install
```

### 2. Run the server

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Open the frontend

In the bottom panel, navigate to PORTS tab.
In the Forwarded Address column, select the "open in browser" icon.
The web site should be open in a new tab

---

### 4. Testing

Open a new termainal tab in codespace.
run

```bash
pytest ./tests/tests.py
```
There are already few tests in the system for API and playwright setup, so it should be easier to continue from here.

Good Luck :)
