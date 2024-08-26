from pathlib import Path

import requests
import aiohttp
from aiohttp import ClientResponseError
from app.file.errors import ResponseError
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

def service_delete_file(name, format):
    file_path = Path(f'app/static/{name}.{format}')
    try:
        file_path.unlink()
    except:
        return