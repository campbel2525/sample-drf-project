from app.core.factories.user_factories import UserFactory, UserMessageCountFactory

from .models import User


class UserSeeder:
    default_password = "test1234"

    def handle(self) -> None:
        password = User.password_to_hash(self.default_password)

        user1 = UserFactory.create(
            email="user1@example.com",
            password=password,
            is_active=True,
            name="user1",
        )
        UserMessageCountFactory.create(user=user1)

        user2 = UserFactory.create()
        UserMessageCountFactory.create(user=user2)

        user3 = UserFactory.create()
        UserMessageCountFactory.create(user=user3)

        user4 = UserFactory.create()
        UserMessageCountFactory.create(user=user4)

        user5 = UserFactory.create()
        UserMessageCountFactory.create(user=user5)
