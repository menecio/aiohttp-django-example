from django.db import models


class Movie(models.Model):
    release_date = models.DateField()
    title = models.CharField(max_length=512)
    rating = models.PositiveSmallIntegerField()
    duration = models.DurationField()
    director = models.CharField(max_length=512)
    genre = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.title} - {self.release_date.year}'
