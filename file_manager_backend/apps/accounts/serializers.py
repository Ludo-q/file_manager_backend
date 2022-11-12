from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import UserFileManager


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFileManager
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
