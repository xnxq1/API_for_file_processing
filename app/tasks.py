import asyncio
from time import sleep

from celery import shared_task
from requests.exceptions import HTTPError
from sqlalchemy import create_engine, insert

from app.celery_config import celery_app
import requests
import threading
from pathlib import Path
from app.config import settings
from app.db import engine
from app.file.models import FileUser
from app.file.repository import RepoFile
from app.file.service import service_delete_file


def download_chunk(url, start, end, file_name, errors):
    headers = {'Range': f'bytes={start}-{end}'}
    try:
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()
        with open(file_name, 'r+b') as file:
            file.seek(start)
            file.write(response.content)
    except BaseException as e:
        errors.append(e)
@shared_task

def download_file(name, format, url, file_size, user_id, num_chunks=4):
    url_for_download = f'app/static/{name}.{format}'
    errors = []
    with open(url_for_download, 'wb') as file:
        file.truncate(file_size)

    chunk_size = file_size // num_chunks
    threads = []

    for i in range(num_chunks):
        start = i * chunk_size
        end = start + chunk_size - 1 if i != num_chunks - 1 else ''
        thread = threading.Thread(target=download_chunk, args=(url, start, end, url_for_download, errors))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    loop = asyncio.get_event_loop()
    if loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    if errors:
        service_delete_file(name=name, format=format)
        loop.run_until_complete(RepoFile.delete_file(name=name, format=format, author_id=user_id))
    else:
        loop.run_until_complete(RepoFile.change_status(True, name=name, format=format, author_id=user_id))









