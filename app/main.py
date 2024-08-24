from fastapi import FastAPI
from app.config import settings
from fastapi.staticfiles import StaticFiles
from app.user.router import router as router_auth
from app.file.router import router as router_file
app = FastAPI()
app.mount('/app/static', StaticFiles(directory='app/static'), name='static')
app.include_router(router_auth)
app.include_router(router_file)
