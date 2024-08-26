from sqlalchemy import insert, update, delete, select

from app.file.models import FileUser
from app.db import async_sessionfactory

class RepoFile:
    model = FileUser
    @classmethod
    async def add_file(cls, **data):
        async with async_sessionfactory() as session:
            stmt = insert(cls.model).values(**data).returning(cls.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    @classmethod
    async def change_status(cls, is_download: bool, **data):
        async with async_sessionfactory() as session:
            stmt = update(cls.model).filter_by(**data).values(is_download=is_download)
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def delete_file(cls, **data):
        async with async_sessionfactory() as session:
            stmt = delete(cls.model).filter_by(**data)
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def get_files(cls, **data):
        async with async_sessionfactory() as session:
            stmt = select(cls.model).filter_by(**data)
            res = await session.execute(stmt)
            return res.scalars().all()

    @classmethod
    async def get_file(cls, **data):
        async with async_sessionfactory() as session:
            stmt = select(cls.model).filter_by(**data)
            res = await session.execute(stmt)
            return res.scalar_one_or_none()