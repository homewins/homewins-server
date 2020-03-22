#!/bin/bash
set -e

echo "Migrate files..."
python manage.py migrate

# Create static files.
python manage.py collectstatic --clear --noinput

if [ "$TYPE" = 'worker' ]; then

    echo "Run gunicorn..."
    gunicorn --bind 0.0.0.0:8800 server.wsgi:application --access-logfile -
elif [ "$TYPE" = 'master' ]; then
    echo "Render nginx.conf..."
    envsubst '\$HOMEWINS_API_WORKER_HOST' < nginx.conf.template > nginx.conf

    echo "Run nginx..."
    cp -r static/ /usr/share/nginx/html
    cp -r nginx.conf /etc/nginx/conf.d/default.conf
    nginx -g 'daemon off;'
else
    echo "Set env TYPE to master/worker."
    exit 1
fi
