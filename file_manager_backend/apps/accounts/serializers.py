from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from rest_framework import serializers

from .models import UserFileManager


class UserFileManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFileManager
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Permission.objects.create(**validated_data)

    class Meta:
        model = Permission
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
