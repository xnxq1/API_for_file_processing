from app.user.repository import RepoUser
from app.user.errors import ThereIsAUserError, WrongDataError
from app.user.auth import Hasher





async def service_register_user(user_data: dict):
        user = await RepoUser.get_user_by_email(user_data['email'])
        if user:
            raise ThereIsAUserError()

        user_data['password'] = Hasher.get_password_hash(user_data['password'])
        try:
            result = await RepoUser.add_user(**user_data)
            return result
        except:
            raise WrongDataError()


async def login_user_service(user_data: dict) -> int:
    user = await RepoUser.get_user_by_email(user_data['email'])
    if not user or not Hasher.verify_password(user_data['password'], user.password):
        raise WrongDataError()
    return user.id
