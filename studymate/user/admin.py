from django.contrib import admin
from .models import User, UserProfile

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('userid', 'password')

admin.site.register(User, UserAdmin)