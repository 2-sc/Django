from django.shortcuts import redirect
import urllib

def kakao_login(request):
    app_rest_api_key = 'c73ac85376ea092795ffebbc710e579b'
    redirect_uri = "http://127.0.0.1:8000/accounts/kakao/login/callback/"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )

def kakao_callback(request):                                                                  
    params = urllib.parse.urlencode(request.GET)                                      
    return redirect(f'http://127.0.0.1:8000/accounts/kakao/login/callback/?{params}')   


