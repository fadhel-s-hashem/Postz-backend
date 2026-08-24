from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer

def create_access_token(user):
    token = RefreshToken.for_user(user).access_token
    token["payload"] = {
        "_id": str(user.id),
        "username": user.username,
    }
    return str(token)
