import pytest
from app.file.repository import RepoFile


@pytest.mark.parametrize('file_id, exists',[
    (1, True),
    (2, True),
    (52, False)
])
async def test_get_file(file_id, exists):
    user = await RepoFile.get_file(id=file_id)
    if not exists:
        assert user is None
    else:
        assert user is not None
        assert user.id == file_id


@pytest.mark.parametrize('name, format, size, author_id, is_download, exception',[
    ('mew', 'json', 21412412, 2, False, False),
    ('mew', 'json', 21412412, 2, False, True),

])
async def test_add_file(name, format, size, author_id, is_download, exception):
    try:
        await RepoFile.add_file(
            name=name, format=format, size=size, author_id=author_id, is_download=is_download)
        if exception:
            assert False
    except:
        if exception:
            assert True
        else:
            assert False

