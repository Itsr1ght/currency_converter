from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .config import BASE_DIR
from .routers import api, templates

app = FastAPI(title="Currency Converter")
app.include_router(api.router)
app.include_router(templates.router)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


@app.get("/robots.txt", include_in_schema=False)
async def robots():
    return FileResponse(BASE_DIR / "static" / "robots.txt", media_type="text/plain")
