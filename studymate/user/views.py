from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import User, UserProfile

# Create your views here.

def home(request): # 로그인 했을 시 username, 안 했을 시 Home 출력
    user_id = request.session.get('user')

    if(user_id):
        user = UserProfile.objects.get(user_id=user_id)
        return HttpResponse(user.username)

    return HttpResponse('Home')

def register(request): # 회원가입 시 문제 없으면 로그인페이지 이동, 문제 있으면 에러메세지 남기고 회원가입 페이지에 머무르기
    if(request.method == 'GET'):
        return render(request, 'register.html')
    elif(request.method == 'POST'):
        userid = request.POST.get('userid', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
    
    res_data = {}

    if not(userid and username and password and re_password):
        res_data['error'] = '아이디 또는 비밀번호를 입력해주세요'
    elif (password != re_password):
        res_data['error'] = '비밀번호가 다릅니다'
    else:
        user = User(
            userid = userid,
            username = username,
            password = password
        )
        user.save()
        return redirect('/user/login')
    return render(request, 'register.html', res_data)

def login(request): # 로그인 성공시 홈페이지로, 실패시 에러메세지 남기고 로그인 페이지 머물기
    if(request.method == 'GET'):
        return render(request, 'login.html')
    elif(request.method == 'POST'):
        userid = request.POST.get('userid', None)
        password = request.POST.get('password', None)

        res_data = {}

        if not(userid and password):
            res_data['error'] = '아이디 또는 비밀번호를 입력해주세요'
        else:
            user = User.objects.get(userid=userid)
            if not user:
                res_data['error'] = '일치하는 아이디가 없습니다'
            elif(password != user.password):
                res_data['error'] = '비밀번호가 일치하지 않습니다'
            else:
                request.session['user'] = user.id
                return redirect('/user/profile')
        return render(request, 'login.html', res_data)


def profile(request): # 홈페이지 로그창에서 프로필 수정..(예정)
    if(request.method == 'GET'):
        return render(request, 'profile.html')
    elif(request.method == 'POST'):
        userid = request.session.get('user')
        user_id = User.objects.get(pk=userid)
        profile_contents = request.POST.get('profile_contents', None)

        res_data = {}

        if not profile_contents:
            res_data['error'] = '프로필을 설정해주세요'
        else:
            user_profile = UserProfile(
                user_id = user_id,
                profile_contents = profile_contents
            )
            user_profile.save()
            return redirect('/')
        return render(request, 'profile.html', res_data)