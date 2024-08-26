from fastapi import HTTPException

from app.errors import BaseCustomError


class ResponseError(BaseCustomError):
    status_code = 400
    message = 'Мы не можем получить положительный запрос на вашу ссылку'
