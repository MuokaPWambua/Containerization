#!/bin/sh

if [ "$BROKER" = "redis" ]
then
    echo "Waiting for redis..."
    while ! nc -zv $BROKER_HOST $BROKER_PORT; do
      sleep 10
    done
    echo "Redis started"
fi
echo "Waiting for app..."
cd app
rm -f celery.pid
touch celery.pid
/home/app/.local/bin/uwsgi --ini uwsgi.ini

exec "$@"
