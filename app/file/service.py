import os
from pathlib import Path

import requests
import aiohttp
from aiohttp import ClientResponseError
from app.file.errors import ResponseError, NotUniqueFileNameError, NoneFileError, NotDownloadFileError
from app.file.repository import RepoFile


async def get_file_size(url):
    try:
        response = await get_headers_from_url(url)
    except ClientResponseError:
        raise ResponseError()
    file_size = int(response.headers['Content-Length'])
    return file_size

async def get_headers_from_url(url):
    async with aiohttp.ClientSession() as session:
        response = await session.head(url)
        response.raise_for_status()
        return response


async def service_delete_file(name, format, user_id):
    file = await RepoFile.get_file(name=name, format=format, author_id=user_id)
    if file is None:
        raise NoneFileError()
    file_dict = file.__dict__
    if not file_dict['is_download']:
        raise NotDownloadFileError()
    await RepoFile.delete_file(name=name, format=format, author_id=user_id)
    file_path = Path(f'app/static/{user_id}_{name}.{format}')
    try:
        file_path.unlink()
    except:
        return


async def service_add_file(**data):
    try:
        await RepoFile.add_file(**data)
    except:
        raise NotUniqueFileNameError()


def get_file_path(name, format, user_id):
    file_path = f"app/static/{user_id}_{name}.{format}"

    if not os.path.exists(file_path):
        raise NoneFileError()
    return file_path