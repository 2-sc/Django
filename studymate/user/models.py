from django.db import models

# Create your models here.

class User(models.Model):
    user = models.CharField(max_length=32, verbose_name='아이디')
    password = models.CharField(max_length=64, verbose_name='비밀번호')

    def __str__(self):
        return self.user
    
    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'


class UserProfile(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')
    username = models.CharField(max_length=32, verbose_name='이름')
    profile_contents = models.TextField(verbose_name='간단한 소개')