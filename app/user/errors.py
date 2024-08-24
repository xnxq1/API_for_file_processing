from app.errors import BaseCustomError


class ThereIsAUserError(BaseCustomError):
    message = "Такой пользователь уже есть"
    status_code = 400



class WrongDataError(BaseCustomError):
    message = "Ошибка валидации данных"
    status_code = 400