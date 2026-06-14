from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend.database import Base, SessionLocal, engine
from backend.models import Achievement, Education, Experience, Profile, Skill
from backend.routers import auth, experiences
from backend.seed import seed_database

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(title="Shaziya Akhtar — Portfolio", version="1.0.0")

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

app.include_router(auth.router)
app.include_router(experiences.router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_database(db)
    finally:
        db.close()


def _portfolio_context(db):
    profile = db.query(Profile).first()
    return {
        "profile": profile,
        "skills": db.query(Skill).order_by(Skill.order_index).all(),
        "experiences": (
            db.query(Experience)
            .order_by(Experience.order_index.desc(), Experience.id.desc())
            .all()
        ),
        "education": db.query(Education).order_by(Education.order_index.desc()).all(),
        "achievements": (
            db.query(Achievement).order_by(Achievement.order_index.desc()).all()
        ),
    }


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    db = SessionLocal()
    try:
        ctx = _portfolio_context(db)
        return templates.TemplateResponse(
            request, "index.html", {"request": request, **ctx}
        )
    finally:
        db.close()


@app.get("/signup", response_class=HTMLResponse)
def signup_page(request: Request):
    return templates.TemplateResponse(request, "signup.html", {"request": request})


@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html", {"request": request})


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard_page(request: Request):
    db = SessionLocal()
    try:
        ctx = _portfolio_context(db)
        return templates.TemplateResponse(
            request, "dashboard.html", {"request": request, **ctx}
        )
    finally:
        db.close()
