from fastapi import APIRouter, UploadFile, File
from fastapi import Depends
from sqlalchemy import select

from app.db import async_sessionfactory
from app.file.models import FileUser
from app.file.repository import RepoFile
from app.file.schemas import FileUpload
from app.file.service import get_file_size
from app.tasks import download_file
from fastapi.responses import StreamingResponse
import requests

from app.user.auth import JWTUser

router = APIRouter(prefix='/file', tags=['Обработка файлов'])

@router.post("/upload")
async def upload_file(file: FileUpload, user=Depends(JWTUser.get_curr_user)):
    file_size = await get_file_size(file.url)
    await RepoFile.add_file(name=file.name, format=file.format, size=file_size, author_id=user.id, is_download=False)
    download_file.apply_async(args=(file.name, file.format, file.url, file_size, user.id))


@router.post("/all")
async def upload_file():
    async with async_sessionfactory() as session:
        query = select(FileUser)
        res = await session.execute(query)
        return res.scalars().all()



