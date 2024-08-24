from fastapi import APIRouter

from app.user.schemas import SchemasUserForRegister, SchemasUser

router = APIRouter(prefix='/auth', tags=['Аутентификация'])

@router.post('/register')
async def register_user(user: SchemasUserForRegister) -> SchemasUser:
    return user