FROM python:3.7-alpine

ENV PYTHONPATH=/app/mymoviedb

ENV PYTHONUNBUFFERED=1

RUN addgroup -S mymoviedb && adduser -h /app/mymoviedb -S mymoviedb -G mymoviedb

COPY --chown=mymoviedb:mymoviedb requirements.txt /app/requirements.txt

RUN apk update --no-cache \
 && apk add --no-cache postgresql-dev \
 && apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    libffi-dev \
 && pip install --no-cache-dir --disable-pip-version-check -r /app/requirements.txt \
 && apk del .build-deps \
 && rm -rf /app/requirements.txt

COPY --chown=mymoviedb:mymoviedb . /app/mymoviedb

WORKDIR /app/mymoviedb

EXPOSE 8000
