import celery
import random

REDIS_URL = "redis://redis:6379"
app = celery.Celery('tasker')
app.conf.update(BROKER_URL=REDIS_URL, CELERY_RESULT_BACKEND=REDIS_URL)


@app.task
def hello(name):
    time.sleep(3)
    return "Hello"