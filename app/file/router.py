from fastapi import APIRouter, UploadFile, File
from fastapi import Depends
from sqlalchemy import select

from app.db import async_sessionfactory
from app.file.models import FileUser
from app.file.repository import RepoFile
from app.file.schemas import FileUpload, SchemasFileForUser
from app.file.service import get_file_size, service_add_file
from app.tasks import download_file
from fastapi.responses import StreamingResponse
import requests

from app.user.auth import JWTUser

router = APIRouter(prefix='/file', tags=['Обработка файлов'])

@router.post("/upload")
async def upload_file(file: FileUpload, user=Depends(JWTUser.get_curr_user)):
    file_size = await get_file_size(file.url)
    await service_add_file(name=file.name, format=file.format, size=file_size, author_id=user.id, is_download=False)
    download_file.apply_async(args=(file.name, file.format, file.url, file_size, user.id))


@router.post("/get_my_file")
async def get_my_file(user=Depends(JWTUser.get_curr_user)) -> list[SchemasFileForUser]:
    files = await RepoFile.get_user_files(user.id)
    return files


