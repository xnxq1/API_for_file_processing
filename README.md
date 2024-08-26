# API_for_file_processing

Тестовое задание:
Задача. Реализовать API со следующим функционалом:
- Регистрация пользователей (поля email, пароль, username, дата рождения, номер телефона).
- Аутентификация пользователей по email и паролю.
- Пользователь должен иметь возможность:
 - Отправить сервису ссылку на (объёмный) файл, который должен быть загружен в фоне при помощи очереди задач.
 - Получить список загруженных пользователем файлов, инфо об одном файле, скачать файл, удалить файл.

- Написать тесты.
- Упаковать в Docker.
- Выложить на GitHub.
- Будет плюсом: задеплоить сервис.

Стек: async FastAPI, async SQLAlchemy, PostgreSQL, pytest. Очередь задач выбрать самостоятельно.

Помощь по запуску:
-----------
Для запуска сервера нужно прописать: 
1. Создать в app папку static
2. docker-compose -f docker-compose-dev.yml build
3. docker-compose -f docker-compose-dev.yml up


Для запуска тестов нужно прописать:
1. docker-compose -f docker-compose-test.yml build
2. docker-compose -f docker-compose-test.yml up

Для запуска unit и integration тестов по отдельности:
docker-compose -f docker-compose-test.yml run test_runner sh -c "pytest -s -v app/tests/unit_tests"

docker-compose -f docker-compose-test.yml run test_runner sh -c "pytest -s -v app/tests/integration_tests"


О проекте:
-----------
.env файл специально открыт, чтобы самостоятельно не заполнять

папка file хранит в себе все связанное с файлами, соответственно папка user хранит всё о юзерах

В данных папках обычно вся логика api в service.py(Сервисный слой), а логика работы с БД в repo.py(Репозиторий/Дао)

Для миграций использовался alembic

Для загрузке файла в фоне используется Celery, таска называется task_download_file
