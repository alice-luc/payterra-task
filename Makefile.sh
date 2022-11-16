#!/bin/sh

docker:
    docker-compose up

migrate:
    python3 manage.py makemigrations && python3 manage.py migrate

static:
    python3 manage.py collectstatic

test:
    pass