# photo > urls.py
from importlib.resources import path
from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photo/new/', views.photo_post, name='photo_post')
]