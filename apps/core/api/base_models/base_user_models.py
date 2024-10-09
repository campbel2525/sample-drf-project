import hashlib

from django.db import models


class BaseUserModel(models.Model):

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
