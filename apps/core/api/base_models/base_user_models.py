import hashlib

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from app.core.base_models.base_auth_user import CustomUserManager


class BaseUserModel(AbstractBaseUser):

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)

    id = models.BigAutoField(
        primary_key=True,
    )
    email = models.CharField(
        max_length=255,
        unique=True,
        db_comment="メールアドレス",
    )
    password = models.CharField(
        max_length=255,
        db_comment="パスワード",
    )
    is_active = models.BooleanField(
        default=True,
        db_comment="アクティブかどうか",
    )
    name = models.CharField(
        max_length=255,
        db_comment="名前",
    )
    post_code = models.CharField(
        max_length=255,
        db_comment="郵便番号",
    )
    country_code = models.CharField(
        max_length=255,
        db_comment="国コード",
    )
    prefecture = models.CharField(
        max_length=255,
        db_comment="都道府県",
    )
    address1 = models.CharField(
        max_length=255,
        db_comment="住所1",
    )
    address2 = models.CharField(
        max_length=255,
        db_comment="住所2",
    )
    tel1 = models.CharField(
        max_length=15,
        db_comment="電話番号1",
    )
    tel2 = models.CharField(
        max_length=15,
        db_comment="電話番号2",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="作成日時",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_comment="更新日時",
    )

    @classmethod
    def password_to_hash(cls, password: str) -> str:
        return hashlib.sha512(password.encode("utf-8")).hexdigest()


class BaseUserMessageCountModel(models.Model):

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)

    id = models.BigAutoField(
        primary_key=True,
    )
    user = models.OneToOneField(
        "users.User",
        on_delete=models.RESTRICT,
        related_name="user_message_count",
    )
    total_count = models.BigIntegerField(
        null=False,
        db_comment="メッセージ数",
    )
    this_month_count = models.BigIntegerField(
        null=False,
        db_comment="メッセージ数",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="作成日時",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_comment="更新日時",
    )
