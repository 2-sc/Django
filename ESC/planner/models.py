from django.db import models

from users.models import User


# Create your models here.
class Planner(models.Model):
    user_email = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=50, verbose_name="todo", blank=True)
    complete = models.BooleanField()
    schedule = models.CharField(max_length=50, verbose_name="schedule", blank=True)
    post_text = models.CharField(max_length=20, verbose_name="post text", blank=True)
    register = models.DateField(verbose_name="today")

    def __str__(self):
        return self.todo
