# Device Manager

A simple full-stack CRUD project for managing network devices. Designed as a QA automation candidate task, this project uses:

- **FastAPI** for the backend
- **Mocked MongoDB (mongomock)** for in-memory storage
- **Mocked Redis (fakeredis)** for caching
- **HTML + JS** frontend

---

## Features

- Add, view, update, and delete devices
- Device data includes `name`, `ip_address`, `status`, and `last_updated`
- Redis caching for `/api/devices` endpoint
- In-memory database and cache: no external services required

---

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
pip install -r requirements.txt
playwright install
```

### 2. Run the server

```bash
uvicorn backend.main:app --reload
```

### 3. Open the frontend

Navigate to:

```
http://localhost:8000/frontend/index.html
```

---

## API Endpoints

- `GET    /api/devices` – Get all devices (cached)
- `POST   /api/device` – Create a new device
- `PUT    /api/device/{id}` – Update existing device
- `DELETE /api/device/{id}` – Delete a device

---

## Running Tests

```bash
pytest tests/
```

- TBD

---

