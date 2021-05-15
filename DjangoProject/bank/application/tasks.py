from application.celery import app


@app.task
def hello():
    with open('log.txt', 'a') as f:
        f.write('hi\n')
