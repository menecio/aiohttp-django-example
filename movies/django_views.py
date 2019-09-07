from django.core.serializers import serialize
from django.http import HttpResponse


from .models import Movie


def movies_list(request):
    queryset = Movie.objects.all()
    content = serialize('json', queryset)
    return HttpResponse(content=content, content_type='application/json')
