from app.core.base_models.base_order_models import BasePaymentModel


class Payment(BasePaymentModel):

    class Meta:
        db_table = "payments"
        db_table_comment = "支払い"
