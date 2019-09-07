# Django ORM from aiohttp
When perfectionists with deadlines meet performance

## :clipboard: Prerequisites
- docker
- docker-compose
- python and django knowledge

## :rocket: Getting started
This project is dockerized, to get it up and running just:
```
docker-compose up -d
```

You will need to run migrations to get your database schema built,
```
docker-compose run --rm --entrypoint python app manage.py migrate
```

and to create a superuser if you want access to `/admin/`:
```
docker-compose run --rm --entrypoint python app manage.py createsuperuser
```

You can load some sample movies:
```
docker-compose run --rm --entrypoint python app manage.py loaddata movies.json
```

## :thought_balloon: Discussion
If you have questions or suggestions, please open an issue (just keep it civilized, please).

## :mega: Disclaimer
Use this at your own risk, this code hasn't been extensibly tested and I'm not responsible for any issues or data loss that could happen if used in a production environment.
