from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    # 관리자 페이지에서 어떤 필드를 보여줄 것인지 설정
    list_display = ('username', 'password')

admin.site.register(User, UserAdmin) # 관리자 사이트에 모델을 등록