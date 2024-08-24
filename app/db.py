from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.mypy.names import DECLARATIVE_BASE

from app.config import settings

engine = create_async_engine(
        settings.DATABASE_URL,
        echo=True,
        pool_size=10,
        future=True)

async_sessionfactory = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

