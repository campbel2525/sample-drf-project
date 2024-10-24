import factory
import pytz
from django.apps import apps
from factory.django import DjangoModelFactory

from .user_factories import UserFactory


class ChatRoomFactory(DjangoModelFactory):

    class Meta:
        model = apps.get_model("chats.ChatRoom")
        skip_postgeneration_save = True

    uuid = factory.Faker("uuid4")
    user = factory.SubFactory(UserFactory)
    name = factory.Faker("sentence", nb_words=3)
    last_message_at = factory.Faker("date_time_this_decade", tzinfo=pytz.UTC)


class ChatMessageFactory(DjangoModelFactory):

    class Meta:
        model = apps.get_model("chats.ChatMessage")
        skip_postgeneration_save = True

    chat_room = factory.SubFactory(ChatRoomFactory)
    message = factory.Faker("paragraph")
    message_token = factory.Faker("random_int", min=0, max=10)
    role = factory.Faker("random_element", elements=["user", "assistant", "system"])
    ai_model_name = factory.Faker("word")
    ai_model_version = factory.Faker("word")
    ai_model_provider = factory.Faker("company")
