from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import User

# Create your views here.

def register(request):
    if(request.method == 'GET'): # 사아트를 접속했을 때
        return render(request, 'register.html') # 회원가입 페이지로 랜더링
    elif(request.method == 'POST'): # 데이터를 입력 후 등록 버튼을 눌렀을 때
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}
        if not(username and useremail and password and re_password):
            res_data['error'] = '값을 입력해주세요!'
        elif(password != re_password):
            res_data['error'] = '비밀번호가 다릅니다!'
        else:
            user = User(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )
            user.save()

        return render(request, 'register.html', res_data)
