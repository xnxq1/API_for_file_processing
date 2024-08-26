from celery import Celery
from app.config import settings


celery_app = Celery(
    'celery_app',
    broker=f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/0'
)
celery_app.autodiscover_tasks(['app.tasks'])