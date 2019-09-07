from django.urls import path

from . import django_views as views


urlpatterns = [path('', views.movies_list), ]
