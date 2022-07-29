from django.shortcuts import render
from .models import User, UserProfile

# Create your views here.

def register(request):
    if(request.method == 'GET'):
        return render(request, 'register.html')
    elif(request.method == 'POST'):
        userid = request.POST.get('userid', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        username = request.POST.get('username', None)
        profile_contents = request.POST.get('profile_contents', None)
    
    res_data = {}

    if not(userid and password and re_password):
        res_data['error'] = '아이디 또는 비밀번호를 입력해주세요'
    elif (password != re_password):
        res_data['error'] = '비밀번호가 다릅니다'
    else:
        user = User(
            userid = userid,
            password = password
        )
        user.save()

        user_profile = UserProfile(
            user_id = userid,
            username = username,
            profile_contents = profile_contents
        )
        user_profile.save()

    return render(request, 'registet.html', res_data)