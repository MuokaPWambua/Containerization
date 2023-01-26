from flask import Flask
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def add(x, y):
    return x + y

@app.route('/add/<int:x>/<int:y>')
def add_route(x, y):
    result = add.delay(x, y)
    return str(result)

if __name__ == '__main__':
    app.run()