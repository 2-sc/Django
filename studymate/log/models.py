from distutils.text_file import TextFile
from django.db import models

# Create your models here.

class Board(models.Model):
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, db_column='writer')
    dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.contents

    class Meta:
        db_table = 'board'
        verbose_name = '담벼락'
        verbose_name_plural = '담벼락'