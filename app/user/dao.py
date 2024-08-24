from sqlalchemy.dialects.mysql import insert

from app.db import async_sessionfactory
from sqlalchemy import select

from app.user.models import User


class RepoUser:
    model = User

    @classmethod
    async def get_user_by_email(cls, email: str):
        async with async_sessionfactory() as session:
            query = select(cls.model).where(cls.model.email==email)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add_user(cls, **data):
        async with async_sessionfactory() as session:
            stmt = insert(cls.model).values(**data).returning(cls.model)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()