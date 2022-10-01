from rest_framework import serializers

from .models import Planner


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planner
        fields = ('todo', 'complete', 'register')
