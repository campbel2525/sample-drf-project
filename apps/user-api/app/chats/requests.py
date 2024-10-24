from rest_framework import serializers


class ChatRoomCreateRequest(serializers.Serializer):
    name = serializers.CharField()


class ChatMessageCreateRequest(serializers.Serializer):
    # chat_room_id = serializers.IntegerField()
    message = serializers.CharField()
