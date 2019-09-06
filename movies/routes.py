from aiohttp import web

from . import views

movies_app = web.Application()

movies_app.add_routes([
    web.get('/', views.movies)
])
