FROM python:3-alpine

# Initialize
RUN mkdir -p /data/web
WORKDIR /data/web
COPY requirements.txt /data/web/

# Setup
RUN apk update
RUN apk upgrade

RUN apk add --update \
    python3 python3-dev postgresql-client \
    postgresql-dev build-base gettext

RUN pip3 install --upgrade pip
RUN pip3 install gunicorn
RUN pip3 install -r requirements.txt

# Clean
RUN apk del -r python3-dev postgresql

# Prepare
COPY . /data/web/

ENV DJANGO_SECRET_KEY="5m$_0$by%6yl(xw6zmh_qsqns*pe-x+5dsel^u+ke$!6h+9jth"
ENV DJANGO_SETTINGS_MODULE=mattdexter.settings
ENV DJANGO_STATIC_ROOT="/data/web/static"
ENV DJANGO_ADMIN_USER="mattdexter"
ENV DJANGO_ADMIN_EMAIL="matt@mattdexter.io"
ENV DJANGO_ADMIN_PASS="mattdexter"

ENV POSTGRES_USER=mattdexter_web
ENV POSTGRES_PASS=mattdexter_web
ENV POSTGRES_SERVICE=postgres
ENV POSTGRES_PORT=5432
ENV POSTGRES_NAME=mattdexter_web

ENV REDIS_SERVICE="redis://redis:6379/0"

ENV GUNICORN_WORKERS=3
ENV GUNICORN_BIND="0.0.0.0:8000"

EXPOSE 8000

RUN chmod 755 ./docker-entrypoint.sh
ENTRYPOINT ["/data/web/docker-entrypoint.sh"]
CMD ["gunicorn", "--config", "gunicorn.conf", "mattdexter.wsgi:application"]