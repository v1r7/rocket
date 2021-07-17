from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from apps.users.models import User

class AuthSerializer(Serializer):
    phone_number = serializers.EmailField(max_length=60)
    password = serializers.CharField(max_length=128)


class UsersListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name', 'email', 'phone_number',
            'is_active' 'is_active'
        )


class UsersCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name', 'email', 'phone_number',
            'is_active', 'password',
        )


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'email', 'date_joined', 'phone_number', 'login', 'action', 'action_wins']

