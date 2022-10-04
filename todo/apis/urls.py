from rest_framework.routers import DefaultRouter
# from django.urls import path

# from .views import ListTodo, DetailTodo
from .views import TodoViewSet
# urlpatterns = [
#     path('', ListTodo.as_view()),
#     path('<int:pk>/', DetailTodo.as_view()),
# ]

router = DefaultRouter()
router.register('', TodoViewSet, basename='todos')
urlpatterns = router.urls
