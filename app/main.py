from fastapi import FastAPI
from app.config import settings
from app.user.router import router as router_auth

app = FastAPI()
app.include_router(router_auth)
