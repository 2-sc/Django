from .models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# 회원가입
class RegisterSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(
        required = True
    )
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password]
    )
    re_password = serializers.CharField(
        write_only = True,
        required = True,
    )

    class Meta:
        model = User
        fields = ('email', 'nickname','password', 're_password')

    def validate(self, value): # validate 추가 설정 -> 비번과 재비번 일치 여부 확인할 길이 없어 추가 설정이 필요
        if(value['password'] != value['re_password']): # 다르면 에러
            raise serializers.ValidationError({"password": "password is not correct!!"})
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            nickname = validated_data['nickname'],
            password = validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user) # create할때 들어가는 user는 장고에서 제공하는 User 모델의 인스턴스가 들어가야한다
        return user

# 로그인
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True, write_only=True)

    def validate(self, value):
        user = authenticate(**value)
        if user:
            token = Token.objects.get(user=user)
            return token
        else:
            raise serializers.ValidationError(
                {'error': '로그인 할 수 없습니다.'}
            )

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'nickname']