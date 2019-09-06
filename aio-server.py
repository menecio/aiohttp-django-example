from aiohttp import web
from django import setup
from django.conf import settings

from mymoviedb import settings as my_settings  # not the same as django.conf.settings
from movies.routes import movies_app


async def setup_django(app):
    settings.configure(
        INSTALLED_APPS=my_settings.INSTALLED_APPS,
        DATABASES=my_settings.DATABASES)
    setup()

app = web.Application()
app.on_startup.append(setup_django)
app.add_subapp('/api/', movies_app)

if __name__ == '__main__':
    web.run_app(app)
