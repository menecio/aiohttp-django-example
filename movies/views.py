from aiohttp import web
from django.apps import apps
from django.core.serializers import serialize

from mymoviedb.utils import database_sync_to_async


async def get_queryset():
    model = apps.get_model('movies.Movie')
    return await database_sync_to_async(model.objects.all)()


async def movies(request):
    queryset = await get_queryset()
    text = serialize('json', queryset)
    return web.json_response(text=text)
