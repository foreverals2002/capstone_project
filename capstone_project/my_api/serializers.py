from rest_framework import serializers

from my_api import models


class FileSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 50)
    filename = serializers.CharField(max_length = 100)
    docfile = serializers.FileField(required=True)

class UserProfileSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 50)
    email = serializers.CharField(max_length = 100)
    password = serializers.CharField(max_length = 50)
    password_confirm = serializers.CharField(max_length = 50)
