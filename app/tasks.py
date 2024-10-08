import asyncio
from concurrent.futures import ThreadPoolExecutor
from time import sleep

from celery import shared_task
from requests.exceptions import HTTPError
from sqlalchemy import create_engine, insert

from app.celery_config import celery_app
import requests
import threading

import multiprocessing
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

#ПОТОКИ В СРЕДНЕМ 140 СЕКУНД НА 1400 МБ ФАЙЛ
@shared_task
def task_download_file(name, format, url, file_size, user_id, num_chunks=4):
    url_for_download = f'app/static/{user_id}_{name}.{format}'
    errors = []
    with open(url_for_download, 'wb') as file:
        file.truncate(file_size)

    chunk_size = file_size // num_chunks
    threads = []

    with ThreadPoolExecutor(max_workers=num_chunks) as executor:
        for i in range(num_chunks):
            start = i * chunk_size
            end = start + chunk_size - 1 if i != num_chunks - 1 else ''
            threads.append(executor.submit(download_chunk, url, start, end, url_for_download, errors))

        # Ждем завершения всех задач
        for thread in threads:
            thread.result()
    loop = asyncio.get_event_loop()
    if loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    if errors:
        service_delete_file(name=name, format=format, user_id=user_id)
        loop.run_until_complete(RepoFile.delete_file(name=name, format=format, author_id=user_id))
    else:
        loop.run_until_complete(RepoFile.change_status(True, name=name, format=format, author_id=user_id))


# ПРОЦЕССЫ В СРЕДНЕМ 186 СЕКУНД НА 1400 МБ ФАЙЛ
# @shared_task
# def task_download_file(name, format, url, file_size, user_id, num_chunks=2):
#     url_for_download = f'app/static/{user_id}_{name}.{format}'
#     errors = []
#     with open(url_for_download, 'wb') as file:
#         file.truncate(file_size)
#
#     chunk_size = file_size // num_chunks
#
#
#     with multiprocessing.Pool(num_chunks) as p:
#         p.starmap(download_chunk, iterable=(
#             (url, i * chunk_size, i * chunk_size + chunk_size - 1 if i != num_chunks - 1 else '', url_for_download, errors)
#             for i in range(num_chunks)))
#         p.close()
#         p.join()
#
#     loop = asyncio.get_event_loop()
#     if loop.is_closed():
#         loop = asyncio.new_event_loop()
#         asyncio.set_event_loop(loop)
#
#     if errors:
#         service_delete_file(name=name, format=format, user_id=user_id)
#         loop.run_until_complete(RepoFile.delete_file(name=name, format=format, author_id=user_id))
#     else:
#         loop.run_until_complete(RepoFile.change_status(True, name=name, format=format, author_id=user_id))

# СТАНДАРТНЫЙ ВАРИАНТ В СРЕДНЕМ 241 СЕКУНД НА 1400 МБ ФАЙЛ
# @shared_task
# def task_download_file(name, format, url, file_size, user_id):
#     url_for_download = f'app/static/{name}.{format}'
#     errors = []
#     with open(url_for_download, 'wb') as file:
#         file.truncate(file_size)
#
#     response = requests.get(url)
#
#     with open(url_for_download, 'wb') as file:
#         file.write(response.content)
#
#     loop = asyncio.get_event_loop()
#     if loop.is_closed():
#         loop = asyncio.new_event_loop()
#         asyncio.set_event_loop(loop)
#
#     if errors:
#         service_delete_file(name=name, format=format, user_id=user_id)
#         loop.run_until_complete(RepoFile.delete_file(name=name, format=format, author_id=user_id))
#     else:
#         loop.run_until_complete(RepoFile.change_status(True, name=name, format=format, author_id=user_id))
#










