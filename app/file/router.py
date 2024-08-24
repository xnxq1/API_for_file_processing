from fastapi import APIRouter, UploadFile


router = APIRouter(prefix='/file', tags=['Обработка файлов'])

@router.post("/upload")
async def upload_file(file_request: UploadFile):
    print(file_request.file)
    print(file_request.filename)