#!/bin/bash

export DJANGO_SETTINGS_MODULE=mattdexter.settings

exec gunicorn mattdexter.wsgi:application \
    --name mattdexter \
    --bind 0.0.0.0:8000 \
    --workers 5 \
"$@"