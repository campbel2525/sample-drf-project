from app.core.factories.chat_factories import ChatMessageFactory, ChatRoomFactory
from app.users.models import User


class ChatSeeder:
    def handle(self) -> None:
        user1 = User.objects.get(id=1)
        chat_room1 = ChatRoomFactory.create(
            user=user1,
        )
        ChatMessageFactory.create(
            chat_room=chat_room1,
            message="あなたはエージェントです。",
            role="system",
        )
        ChatMessageFactory.create(
            chat_room=chat_room1,
            message="こんにちは",
            role="user",
        )
        ChatMessageFactory.create(
            chat_room=chat_room1,
            message="こんにちは。要件はなんですか？",
            role="assistant",
        )
        chat_room2 = ChatRoomFactory.create(
            user=user1,
        )
        ChatMessageFactory.create(
            chat_room=chat_room2,
            message="こんにちは",
            role="user",
        )
        ChatMessageFactory.create(
            chat_room=chat_room2,
            message="こんにちは。要件はなんですか？",
            role="assistant",
        )

        user2 = User.objects.get(id=2)
        chat_room3 = ChatRoomFactory.create(
            user=user2,
        )
        ChatMessageFactory.create(
            chat_room=chat_room3,
            message="こんにちは",
            role="user",
        )
        ChatMessageFactory.create(
            chat_room=chat_room3,
            message="こんにちは。要件はなんですか？",
            role="assistant",
        )
