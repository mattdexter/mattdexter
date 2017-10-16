FROM python:3.5-alpine

RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/

RUN apk update
RUN apk upgrade

RUN apk add --update \
    python3 python3-dev postgresql-client \
    postgresql-dev build-base gettext curl

RUN pip install -r requirements.txt

RUN apk del -r python3-dev postgresql

COPY . /src/

CMD ["gunicorn", "--config", "gunicorn.conf", "mattdexter.wsgi:application"]