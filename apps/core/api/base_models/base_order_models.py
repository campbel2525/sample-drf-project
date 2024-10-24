from django.db import models


class BasePaymentModel(models.Model):

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)

    id = models.BigAutoField(
        primary_key=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.RESTRICT,
        related_name="payments",
        null=True,
    )
    amount = models.BigIntegerField(
        db_comment="支払金額",
    )
    tax = models.IntegerField(
        db_comment="税額",
    )
    total_amount = models.IntegerField(
        db_comment="総支払額",
    )
    payment_at = models.DateTimeField(
        db_comment="支払日",
    )

    user_country_code = models.CharField(
        max_length=255,
        db_comment="ユーザーの国コード",
    )
    user_email = models.CharField(
        max_length=255,
        db_comment="ユーザーのメールアドレス",
    )
    user_name = models.CharField(
        max_length=255,
        db_comment="ユーザーの名前",
    )
    user_post_code = models.CharField(
        max_length=255,
        db_comment="ユーザーの郵便番号",
    )
    user_prefecture = models.CharField(
        max_length=255,
        db_comment="ユーザーの都道府県",
    )
    user_address1 = models.CharField(
        max_length=255,
        db_comment="ユーザーの住所1",
    )
    user_address2 = models.CharField(
        max_length=255,
        db_comment="ユーザーの住所2",
    )
    user_tel1 = models.CharField(
        max_length=15,
        db_comment="ユーザーの電話番号1",
    )
    user_tel2 = models.CharField(
        max_length=15,
        db_comment="ユーザーの電話番号2",
    )

    company_country_code = models.CharField(
        max_length=255,
        db_comment="会社の国コード",
    )
    company_name = models.CharField(
        max_length=255,
        db_comment="会社の名前",
    )
    company_post_code = models.CharField(
        max_length=255,
        db_comment="会社の郵便番号",
    )
    company_prefecture = models.CharField(
        max_length=255,
        db_comment="会社の都道府県",
    )
    company_address1 = models.CharField(
        max_length=255,
        db_comment="会社の住所1",
    )
    company_address2 = models.CharField(
        max_length=255,
        db_comment="会社の住所2",
    )
    company_tel1 = models.CharField(
        max_length=15,
        db_comment="会社の電話番号1",
    )
    company_tel2 = models.CharField(
        max_length=15,
        db_comment="会社の電話番号2",
    )

    stripe_code = models.CharField(
        max_length=255,
        unique=True,
        db_comment="Stripeのコード",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_comment="作成日時",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_comment="更新日時",
    )
