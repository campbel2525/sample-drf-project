from app.core.base_models.base_chat_models import (
    BaseChatMessageModel,
    BaseChatRoomModel,
)


class ChatRoom(BaseChatRoomModel):

    class Meta:
        db_table = "chat_rooms"
        db_table_comment = "チャットルーム"


class ChatMessage(BaseChatMessageModel):

    class Meta:
        db_table = "chat_messages"
        db_table_comment = "チャットメッセージ"
