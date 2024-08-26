from datetime import datetime

import pytest
from httpx import AsyncClient

router_prefix = '/auth'

@pytest.mark.parametrize('email, password, username, date_of_birth, phone_number, status_code',[
    ('rabota1@mail.com', 'password', 'Justin Bearer', '2010-09-26', '+325235253', 200),
    ('robot1@pycharm.com', '123123', 'Justin Test', '2000-09-26', '+565235253', 200),
    (1, 'password', 'Justin Bearer', '2010-09-26', '+325235253', 422),
    ('ro111bot1@pycharm.com', '123123', 'Justin Test', '2000-09-26', '565235253', 422),
    ('123@pycharm.com', '123123', 'Justin Test', '2000-09-26', '+42342342343242342323', 422),
    ('234@pycharm.com', '123123', 'Justin Test', '2000-09-26', '+dsfsdfsdsdf', 422),
])
async def test_register_user(email, password, username, date_of_birth, phone_number, status_code, async_client: AsyncClient):
    url = f'{router_prefix}/register'
    response = await async_client.post(url=url, json={
        'email': email, 'password': password, 'username': username, 'date_of_birth': date_of_birth, 'phone_number': phone_number})
    assert response.status_code == status_code



@pytest.mark.parametrize('email, password, status_code', [
    ('test1@test.com', 'test', 200),
    ('test2@test.com', 'test', 200),
    ('ivan@test.com', 'wrong', 400),
    ('test2@test.com', 'tes11t', 400),
    ('test2test.com', 'tes11t', 422),

])
async def test_login_user(email, password, status_code, async_client: AsyncClient):
    url = f'{router_prefix}/login'
    response = await async_client.post(url=url, json={
        'email': email, 'password': password
    })

    assert response.status_code == status_code
    if status_code == 200:
        assert response.cookies.get('access_token') is not None


async def test_logout_user(authenticate_client: AsyncClient):
    url = f'{router_prefix}/logout'
    response = await authenticate_client.post(url=url)

    assert response.status_code == 200
    assert response.cookies.get('access_token') is None

    response = await authenticate_client.post(url=url)
    assert response.status_code == 401
