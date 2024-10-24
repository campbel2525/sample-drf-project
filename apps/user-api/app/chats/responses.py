from rest_framework import serializers


class ChatRoomResponse(serializers.Serializer):
    # id = serializers.IntegerField()
    uuid = serializers.CharField()
    name = serializers.CharField()
    last_message_at = serializers.DateTimeField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class ChatRoomMessageResponse(serializers.Serializer):
    # id = serializers.IntegerField()
    message = serializers.CharField()
    message_token = serializers.IntegerField()
    role = serializers.CharField()
    ai_model_name = serializers.CharField()
    ai_model_version = serializers.CharField()
    ai_model_provider = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
