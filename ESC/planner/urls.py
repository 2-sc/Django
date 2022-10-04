from django.urls import path
from .views import TodoAPIView, TodoCreateAPIView, TodoDetailAPIView

urlpatterns = [
    # path('todo/', TodosAPIView.as_view())
    path('', TodoAPIView.as_view()),
    path('todo/post/', TodoCreateAPIView.as_view()),
    path('todo/<int:pk>/', TodoDetailAPIView.as_view())
]
