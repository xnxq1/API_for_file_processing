
from fastapi import APIRouter, Response, Request

from app.user.auth import JWTCookies
from app.user.schemas import SchemasUserForRegister, SchemasUser, SchemasUserForAuth
from app.user.service import service_register_user, login_user_service

router = APIRouter(prefix='/auth', tags=['Аутентификация'])

@router.post('/register')
async def register_user(user: SchemasUserForRegister) -> SchemasUser:
    user_data = dict(user)
    return await service_register_user(user_data)


@router.post("/login")
async def login_user(request: Request, responce: Response, user: SchemasUserForAuth) -> str:

    user_id = await login_user_service(dict(user))
    return JWTCookies.set_cookie_jwt(responce, user_id)


@router.post("/logout")
async def logout_user(request: Request, responce: Response) -> None:
    JWTCookies.delete_cookie_jwt(request, responce)