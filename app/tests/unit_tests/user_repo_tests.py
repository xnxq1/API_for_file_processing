from datetime import datetime

import pytest

from app.user.repository import RepoUser


@pytest.mark.parametrize('email, exists',[
    ('test1@test.com', True),
    ('test2@test.com', True),
    ('wewefweffw', False)
])
async def test_get_user_by_email(email, exists):
    user = await RepoUser.get_user_by_email(email)
    if not exists:
        assert user is None
    else:
        assert user is not None
        assert user.email == email



@pytest.mark.parametrize('user_id, exists',[
    (1, True),
    (2, True),
    (100, False)
])
async def test_get_user_by_id(user_id, exists):
    user = await RepoUser.get_user_by_id(user_id)
    if not exists:
        assert user is None
    else:
        assert user is not None
        assert user.id == user_id


@pytest.mark.parametrize('email, password, username, date_of_birth, phone_number, exception',[
    ('rabota@mail.com', 'password', 'Justin Bearer', '2010-09-26', '+325235253', False),
    ('robot@pycharm.com', '123123', 'Justin Test', '2000-09-26', '+565235253', False),
    ('mail@mail.com', 'mail', 'Justin Mail', '2006-09-26', '+87876856', False),
    ('rabota@mail.com', 'password', 'Justin Bearer', '2010-09-26', '+325235253', True),
])
async def test_add_user(email, password, username, date_of_birth, phone_number, exception):
    try:
        date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')
        user = await RepoUser.add_user(
            email=email, password=password, username=username, date_of_birth=date_of_birth, phone_number=phone_number)
        if exception:
            assert False
        else:
            assert user is not None
            assert user.email == email
    except:
        if exception:
            assert True
        else:
            assert False

