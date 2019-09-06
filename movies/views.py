from aiohttp import web
from django.apps import apps
from django.core.serializers import serialize

from mymoviedb.utils import database_sync_to_async

routes = web.RouteTableDef()


@routes.view('/movies')
class MoviesView(web.View):
    model = 'movies.Movie'

    async def get_queryset(self):
        model = apps.get_model(self.model)
        return await database_sync_to_async(model.objects.all)()

    async def get(self):
        queryset = await self.get_queryset()
        text = serialize('json', queryset)
        return web.json_response(text=text)
