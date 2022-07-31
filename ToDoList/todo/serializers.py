#  todo > serializers.py
from rest_framework import serializers
from .models import Todo

class TodoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        # 모델 클래스 내에 위치, 장고의 모델에 취급하는 방법을 변경할 수 있다
        # 예약된 속성을 써서 '값'으로 초기화하는 것으로 변경이 가능하다
        model = Todo
        fields = ('id', 'title', 'complete','important')