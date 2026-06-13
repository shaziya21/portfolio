# Portfolio

A modern, minimal portfolio site for Shaziya Akhtar with FastAPI backend, JWT authentication, and experience management.

## Setup

Requires Python 3.12 or 3.13.

```bash
cd portfolio
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Open [http://localhost:8000](http://localhost:8000) for the portfolio.

## Admin

1. Go to [http://localhost:8000/signup](http://localhost:8000/signup) to create an account
2. Sign in at [http://localhost:8000/login](http://localhost:8000/login)
3. Manage experiences at [http://localhost:8000/dashboard](http://localhost:8000/dashboard)

## API

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/auth/signup` | No | Create account |
| POST | `/api/auth/login` | No | Get JWT token |
| GET | `/api/experiences` | No | List experiences |
| POST | `/api/experiences` | Yes | Add experience |
| PUT | `/api/experiences/{id}` | Yes | Update experience |
| DELETE | `/api/experiences/{id}` | Yes | Delete experience |

## Stack

- **Backend:** FastAPI, SQLAlchemy, SQLite, JWT
- **Frontend:** HTML, CSS, Jinja2 templates
