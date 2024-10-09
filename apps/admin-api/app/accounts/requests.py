from rest_framework import serializers


class LoginRequest(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)


class RefreshRequest(serializers.Serializer):
    refresh_token = serializers.CharField()
