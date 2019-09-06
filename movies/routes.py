from aiohttp import web

from . import views

movies_app = web.Application()
movies_app.router.add_routes(views.routes)
