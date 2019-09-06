from django.apps import apps

from .utils import database_sync_to_async


class ModelMixin:
    model = None

    async def get_queryset(self, **kwargs):
        model = apps.get_model(self.model)
        return await database_sync_to_async(model.objects.filter)(**kwargs)
