import os

from aiohttp import web
from django import setup
from django.conf import settings

from mymoviedb.settings import BASE_DIR
from movies.routes import movies_app


async def setup_django(app):
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        },
        INSTALLED_APPS=['movies']
    )
    setup()

app = web.Application()
app.on_startup.append(setup_django)
app.add_subapp('/movies/', movies_app)

if __name__ == '__main__':
    web.run_app(app)
