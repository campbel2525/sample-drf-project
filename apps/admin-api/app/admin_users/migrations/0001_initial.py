# Generated by Django 5.1.2 on 2024-11-23 06:15

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdminUser",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "email",
                    models.CharField(
                        db_comment="メールアドレス", max_length=255, unique=True
                    ),
                ),
                ("password", models.CharField(db_comment="パスワード", max_length=255)),
                (
                    "is_active",
                    models.BooleanField(db_comment="アクティブかどうか", default=True),
                ),
                ("name", models.CharField(db_comment="名前", max_length=255)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, db_comment="作成日時"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, db_comment="更新日時"),
                ),
            ],
            options={
                "db_table": "admin_users",
                "db_table_comment": "管理者ユーザー",
            },
        ),
        migrations.CreateModel(
            name="AdminUserOneTimePassword",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "uuid",
                    models.UUIDField(
                        db_comment="ワンタイムパスワードUUID",
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                    ),
                ),
                (
                    "is_used",
                    models.BooleanField(db_comment="使用済みかどうか", default=False),
                ),
                ("type", models.CharField(db_comment="種類 login", max_length=255)),
                (
                    "one_time_password",
                    models.CharField(db_comment="1回限りのトークン", max_length=255),
                ),
                (
                    "new_email",
                    models.CharField(
                        db_comment="新しいメールアドレス",
                        default=None,
                        max_length=255,
                        null=True,
                    ),
                ),
                ("expires_at", models.DateTimeField(db_comment="有効期限")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, db_comment="作成日時"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, db_comment="更新日時"),
                ),
                (
                    "admin_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="admin_user_one_time_passwords",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "admin_user_one_time_passwords",
                "db_table_comment": "管理者ユーザー",
            },
        ),
    ]