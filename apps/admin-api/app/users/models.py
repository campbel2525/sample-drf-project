from app.core.base_models.base_user_models import (
    BaseUserMessageCountModel,
    BaseUserModel,
)


class User(BaseUserModel):

    class Meta:
        db_table = "users"
        db_table_comment = "ユーザー"


class UserMessageCount(BaseUserMessageCountModel):

    class Meta:
        db_table = "user_message_counts"
        db_table_comment = "ユーザーメッセージ数"
