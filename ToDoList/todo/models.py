# todo > models.py
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 100)          # Todo의 제목
    description = models.TextField(blank = True)        # Todo에 대한 설명
    created = models.DateTimeField(auto_now_add = True) # Todo 생성 일자 -> 스터디 메이트X
    complete = models.BooleanField(default = False)     # Todo 완료 여부
    important = models.BooleanField(default = False)    # Todo 중요 여부 -> 스터디 메이트X

    # __str__: 내가 입력한 값 그대로를 출력하여 보고싶을 때 이 함수를 사용한다[모델 클래스의 객체를 문자열로]
    def __str__(self):
        return self.title