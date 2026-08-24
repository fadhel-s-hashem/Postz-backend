from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Comment, Postz

class UserSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(source="pk", read_only=True)

    class Meta:
        model = User
        fields = ["_id", "username"]


