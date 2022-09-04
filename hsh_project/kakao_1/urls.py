from django.urls import path
from . import views

urlpatterns = [
    path('account/login/kakao/', views.kakao_login, name='kakao_login'),
    path('account/login/kakao/callback/', views.kakao_callback, name='kakao_callback'),
    #path('accounts/kakao/login/finish/', views.KakaoLogin.as_view(), name='kakao_login_todjango'),
    
]