from fastapi import FastAPI
from app.config import settings

app = FastAPI()

@app.get('/')
async def start():
    return settings.DATABASE_URL