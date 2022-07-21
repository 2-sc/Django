from django.db import models
from django.forms import CharField, DateTimeField

# Create your models here.

# 해당 모델에 데이터가 추가되면 그 데이터를 문자열로 반환해서 보여줌
# 모델이 클래스이기 때문에 데이터가 추가되면 객체로 생성되어 문자열로 변환하면 User object 라는 문자열로 보여줌
# 문자열로 유저를 쉽게 알아보기 힘들기 때문에 문자열로 변환 할 때 추가 작업이 필요
class User(models.Model):
    username = models.CharField(max_length=32, verbose_name='유저이름')
    useremail = models.EmailField(max_length=128, verbose_name='사용자이메일')
    password = models.CharField(max_length=64, verbose_name='패스워드')
    register_dttm = models.DateTimeField(verbose_name='등록시간', auto_now_add=True)

    def __str__(self): # 문자열로 변환할 때 호출되는 함수
        # 객체에서 문자열로 변환할 때 해당 객체의 유저이름을 리턴
        # User object 대신 유저이름을 보여줌
        return self.username
        
    class Meta:
        db_table = 'hsh_userinfo' # sql 테이블명
        verbose_name = '사용자' # 관리자 페이지에서 User 대신 보여지는 이름(단수)
        verbose_name_plural = '사용자' # 관리자 페이지에서 User 대신 보여지는 이름(복수)
        
    