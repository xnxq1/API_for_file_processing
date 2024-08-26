from datetime import datetime

import pytest
import os
from httpx import AsyncClient, ASGITransport
from sqlalchemy import insert

from app.main import app as fastapi_app
from app.db import engine, async_sessionfactory
from app.models import Base
import json

from app.user.models import User


@pytest.fixture(autouse=True, scope='session')
async def prepare_db():
    assert os.environ['MODE'] == 'TEST'
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def convert_json(model: str):
        with open(f'app/tests/{model}.json') as f:
            return json.load(f)

    users = convert_json('users')
    for user in users:
        user['date_of_birth'] = datetime.strptime(user['date_of_birth'], '%Y-%m-%d')
    async with async_sessionfactory() as session:
        users_query = insert(User).values(users)
        await session.execute(users_query)
        await session.commit()



@pytest.fixture(scope='function')
async def async_client():
    async with AsyncClient(transport=ASGITransport(app=fastapi_app), base_url='http://test') as ac:
        yield ac


@pytest.fixture(scope='function')
async def authenticate_client():
    async with AsyncClient(transport=ASGITransport(app=fastapi_app), base_url='http://test') as ac:
        await ac.post(url='auth/login', json={
        'email': 'test1@test.com', 'password': 'test'})
        assert ac.cookies.get('access_token') is not None
        yield ac
