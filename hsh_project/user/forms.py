from django import forms
from .models import User
from django.contrib.auth.hashers import check_password

class Loginform(forms.Form):
    # 값 변경/검사 및 html 코드에 랜더링할 데이터 설정
    username = forms.CharField(
        error_messages={
            # 상황별 에러메세지 설정
            'required': '아이디를 입력해주세요.'
        },
        max_length=32, label='사용자 이름')
    password = forms.CharField(
        error_messages={
            # 상황별 에러메세지 설정 
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호')

    def clean(self):
        # 값이 비어있는지 검사하는 메소드. 값이 있으면 필드 이름을 키로 하는 cleaned_data 딕셔너리에 추가
        cleaned_data = super().clean() 
        username = cleaned_data.get('username') # 딕셔너리에서 username 키 값 가져오기
        password = cleaned_data.get('password') # cleaned_data에서 password 키 값 가져오기

        if username and password: # 값이 둘다 존재한다면
            user = User.objects.get(username=username) # username 과 일치하는 유저 객체 불러오기
            if not check_password(password, user.password): # 입력한 password 와 유저 password 가 다르면
                self.add_error('password', '비밀번호를 틀렸습니다') # password 필드에 에러 메세지 추가
            else: # 에러가 없으면
                self.user_id = user.id # 해당 유저 아이디 값을 폼을 호출한 유저의 아이디에 저장
