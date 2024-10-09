from django.db import connection

from app.core.base_models.base_user_models import BaseUserModel


class User(BaseUserModel):

    class Meta:
        db_table = "users"
        managed = False

    def check_password(self, raw_password: str) -> bool:
        return self.password == User.password_to_hash(raw_password)

    def count_up_message_count(self):
        sql = """
            UPDATE user_message_counts
            SET total_count = total_count + 1, this_month_count = this_month_count + 1
            WHERE id = %s
        """

        with connection.cursor() as cursor:
            cursor.execute(sql, [self.id])
