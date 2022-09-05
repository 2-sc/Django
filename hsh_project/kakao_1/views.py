from django.shortcuts import redirect
import urllib
from django.views import View
from django.http import JsonResponse
import requests



class kakaoSignInView(View):
    def get(self, request):
        app_rest_api_key = 'c73ac85376ea092795ffebbc710e579b'
        redirect_uri = 'http://127.0.0.1:8000/account/kakao/login/callback'
        return redirect(
            f"https://kauth.kakao.com/oauth/authorize?client_id=${app_rest_api_key}&redirect_uri=${redirect_uri}&response_type=code"
        )

class KaKaoSignInCallBackView(View):
    def get(self, request):
        auth_code = request.GET.get('code')
        kakao_token_api = 'https://kauth.kakao.com/oauth/token'
        data = {
            'grant_type': 'authorization_code',
            'client_id': 'c73ac85376ea092795ffebbc710e579b',
            'redirection_uri': 'http://localhost:8000/accounts/signin/kakao/callback/',
            'code': auth_code
        }
        
        token_response = requests.post(kakao_token_api, data=data)
        
        access_token = token_response.json().get('access_token')
        
        user_info_response = requests.get('https://kapi.kakao.com/v2/user/me', headers={"Authorization": f'Bearer ${access_token}'})
        
        return JsonResponse({"user_info": user_info_response.json()})

