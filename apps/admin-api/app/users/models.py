from app.core.base_models.base_user_models import BaseUserModel


class User(BaseUserModel):

    class Meta:
        db_table = "users"
        db_table_comment = "ユーザー"
