import uuid
from datetime import datetime

from django.conf import settings
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import ChatMessage, ChatRoom
from .requests import ChatMessageCreateRequest, ChatRoomCreateRequest
from .responses import ChatRoomMessageResponse, ChatRoomResponse
from .usecases.chat_usecases import chat_usecase


class ChatRoomView(viewsets.ViewSet):
    def list(self, request):
        user = request.user
        chat_rooms = (
            ChatRoom.objects.filter(user=user).order_by("-last_message_at").all()
        )
        serializer = ChatRoomResponse(chat_rooms, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def retrieve(self, request, uuid):
        user = request.user

        chat_room = get_object_or_404(ChatRoom, user=user, uuid=uuid)
        serializer = ChatRoomResponse(chat_room)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ChatRoomCreateRequest(data=request.data)
        serializer.is_valid(raise_exception=True)

        chat_room = ChatRoom()
        chat_room.uuid = uuid.uuid4()
        chat_room.user = request.user
        chat_room.name = request.data.get("name")
        chat_room.last_message_at = datetime.now()
        chat_room.save()

        return self.retrieve(request, chat_room.id)

    def destroy(self, request, uuid):
        user = request.user
        chat_room = get_object_or_404(ChatRoom, user=user, uuid=uuid)

        with transaction.atomic():
            chat_room.chat_messages.all().delete()
            chat_room.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ChatMessageView(viewsets.ViewSet):
    def list(self, request, chat_room_uuid):
        user = request.user
        chat_room = get_object_or_404(ChatRoom, user=user, uuid=chat_room_uuid)
        chat_room_messages = ChatMessage.objects.filter(chat_room=chat_room).all()

        serializer = ChatRoomMessageResponse(chat_room_messages, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def create(self, request, chat_room_uuid):
        serializer = ChatMessageCreateRequest(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        chat_room = get_object_or_404(ChatRoom, user=user, uuid=chat_room_uuid)

        # チャット && データ保存
        result = chat_usecase(
            chat_room,
            request.data.get("message"),
            settings.AI_MODEL_NAME,
        )

        serializer = ChatRoomMessageResponse(result["ai_chat_message"])
        return Response(serializer.data, status=status.HTTP_200_OK)
