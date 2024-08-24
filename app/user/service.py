from app.user.dao import RepoUser
from app.user.errors import ThereIsAUserError, WrongDataError

from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)


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
