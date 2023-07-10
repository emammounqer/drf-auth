# LAB - Class 33

## Project: Authentication & Production Server

## Author: Emam Al Mounqer

## Setup

you need to have docker installed on your machine

```bash
docker compose up
```

## How to initialize/run your application

```bash
docker compose run web python manage.py migrate

docker compose run web python manage.py createsuperuser
```

## Tests

```bash
python manage.py test
```
