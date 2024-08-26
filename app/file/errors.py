from fastapi import HTTPException

from app.errors import BaseCustomError


class ResponseError(BaseCustomError):
    status_code = 400
    message = 'Мы не можем получить положительный запрос на вашу ссылку'

class NotUniqueFileNameError(BaseCustomError):
    status_code = 400
    message = 'У вас уже есть файл с таким именем и форматом'

class NoneFileError(BaseCustomError):
    status_code = 400
    message = 'Такого файла не существует'


class NotDownloadFileError(BaseCustomError):
    status_code = 400
    message = 'Файл можно удалить только после полного скачивания'
