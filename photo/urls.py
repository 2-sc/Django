from importlib.resources import path
from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path('', views.photo_list, name='photo_list')
]