from django.db import models


class Movie(models.Model):
    release_date = models.DateField()
    title = models.CharField(max_length=512)
    rating = models.PositiveSmallIntegerField()
    duration = models.DurationField()
    director = models.CharField(max_length=512)

    class Meta:
        app_label = 'movies'
