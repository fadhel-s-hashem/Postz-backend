from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Comment, Postz

class UserSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(source="pk", read_only=True)

    class Meta:
        model = User
        fields = ["_id", "username"]



class PostzSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(source="pk", read_only=True)
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    createdAt = serializers.DateTimeField(
        source="created_at",
        read_only=True,
    )

    class Meta:
        model = Postz
        fields = [
            "_id",
            "title",
            "text",
            "category",
            "author",
            "comments",
            "createdAt",
        ]


class CommentSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(source="pk", read_only=True)
    author = UserSerializer(read_only=True)
    createdAt = serializers.DateTimeField(
        source="created_at",
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ["_id", "text", "author", "createdAt"]
