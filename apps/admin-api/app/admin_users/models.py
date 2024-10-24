from app.core.base_models.base_admin_user_models import BaseAdminUserModel


class AdminUser(BaseAdminUserModel):

    class Meta:
        db_table = "admin_users"
        db_table_comment = "管理者ユーザー"

    def check_password(self, raw_password: str) -> bool:
        return self.password == AdminUser.password_to_hash(raw_password)
