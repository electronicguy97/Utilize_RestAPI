# Todo 앱에 직렬화를 위한 serializers.py 파일을 생성하고 TodoSerializer를 정의
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'