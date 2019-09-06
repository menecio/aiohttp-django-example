import json

from aiohttp import web
from django.apps import apps
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder

from mymoviedb.utils import database_sync_to_async

routes = web.RouteTableDef()


@routes.view('/movies')
class MoviesListView(web.View):
    model = 'movies.Movie'

    async def get_queryset(self):
        model = apps.get_model(self.model)
        return await database_sync_to_async(model.objects.all)()

    async def get(self):
        queryset = await self.get_queryset()
        text = serialize('json', queryset)
        return web.json_response(text=text)


@routes.view('/movies/{pk}')
class MoviesDetailView(web.View):
    model = 'movies.Movie'

    async def get_queryset(self, **kwargs):
        model = apps.get_model(self.model)
        return await database_sync_to_async(model.objects.filter)(**kwargs)

    async def get(self):
        pk = self.request.match_info['pk']
        queryset = await self.get_queryset(pk=pk)
        movie = queryset.values().first()

        if not movie:
            return web.json_response(data={'message': 'Not found'}, status=404)

        text = json.dumps(movie, cls=DjangoJSONEncoder)
        return web.json_response(text=text)
