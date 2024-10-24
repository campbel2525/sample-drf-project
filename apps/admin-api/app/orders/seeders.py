from app.core.factories.orders_factories import PaymentFactory
from app.users.models import User


class PaymentSeeder:
    def handle(self) -> None:
        user1 = User.objects.get(id=1)
        user2 = User.objects.get(id=2)

        PaymentFactory.create(
            user=user1,
        )
        PaymentFactory.create(
            user=user1,
        )
        PaymentFactory.create(
            user=user2,
        )
        PaymentFactory.create(
            user=user2,
        )
