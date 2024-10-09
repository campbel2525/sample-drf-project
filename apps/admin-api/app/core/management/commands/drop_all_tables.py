from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = "データベースの全てのテーブルを削除します"

    def handle(self, *args, **kwargs) -> None:
        if not settings.DEBUG:
            print("デバッグ環境でないため実行できません")
            return

        with connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

        table_names = connection.introspection.table_names()
        for table_name in table_names:
            with connection.cursor() as cursor:
                cursor.execute(f"DROP TABLE {table_name} CASCADE")

        with connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
