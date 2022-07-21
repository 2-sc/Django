from django import views
from django.urls import path
from . import views

urlpatterns = [
    # 앱의 url 세팅
    # 뷰 연동 -> user/ 이후 register/ 을 작성하면 views 에 있는 register 함수 불러온다.
    path('register/',views.register)
]
