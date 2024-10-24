from django.db import models


class BaseChatRoomModel(models.Model):

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)

    id = models.BigAutoField(
        primary_key=True,
    )
    uuid = models.CharField(
        max_length=255,
        db_comment="チャットルームUUID",
        unique=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.RESTRICT,
        related_name="chat_rooms",
    )
    name = models.CharField(
        max_length=255,
        db_comment="チャットルーム名",
    )
    last_message_at = models.DateTimeField(
        db_comment="最終メッセージ日時",
        db_index=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="作成日時",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_comment="更新日時",
    )


class BaseChatMessageModel(models.Model):

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)

    id = models.BigAutoField(
        primary_key=True,
    )
    chat_room = models.ForeignKey(
        "chats.ChatRoom",
        on_delete=models.RESTRICT,
        related_name="chat_messages",
    )
    message = models.TextField(
        db_comment="メッセージ内容",
    )
    message_token = models.IntegerField(
        db_comment="メッセージタイプ",
    )
    role = models.CharField(
        max_length=255,
        db_comment="メッセージの役割",
    )

    ai_model_name = models.CharField(
        max_length=255,
        db_comment="AIモデル名",
    )
    ai_model_version = models.CharField(
        max_length=255,
        db_comment="AIモデルバージョン",
    )
    ai_model_provider = models.CharField(
        max_length=255,
        db_comment="AIモデルプロバイダー",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="作成日時",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_comment="更新日時",
    )
