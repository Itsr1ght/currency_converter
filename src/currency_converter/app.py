from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .routers import api

BASE_DIR = Path(__file__).parent


app = FastAPI(title="Currency Converter")
app.include_router(api.router)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/robots.txt", include_in_schema=False)
async def robots():
    return FileResponse(BASE_DIR / "static" / "robots.txt", media_type="text/plain")


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="home.html")
