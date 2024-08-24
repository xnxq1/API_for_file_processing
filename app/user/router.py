from fastapi import APIRouter
from app.user.schemas import SchemasUserForRegister, SchemasUser
from app.user.service import service_register_user

router = APIRouter(prefix='/auth', tags=['Аутентификация'])

@router.post('/register')
async def register_user(user: SchemasUserForRegister) -> SchemasUser:
    user_data = user.__dict__
    return await service_register_user(user_data)

