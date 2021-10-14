from rest_framework import serializers

from my_api import models


class FileSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 50)
    filename = serializers.CharField(max_length = 100)
