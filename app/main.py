from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from app.api.points import router as points_router

app = FastAPI(title="InPost Smart Locker API")
app.include_router(points_router, prefix="/points")
app.mount("/ui", StaticFiles(directory="app/ui"), name="ui")

@app.get("/")
async def root():
    return RedirectResponse(url="/ui/page.html")