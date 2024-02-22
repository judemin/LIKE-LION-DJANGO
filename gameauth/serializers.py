from rest_framework import serializers
from gameauth.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("id", "name", "email", "password", "bestScore")
