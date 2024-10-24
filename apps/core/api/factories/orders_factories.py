import importlib
import random

import factory
import pytz
from django.apps import apps
from factory.django import DjangoModelFactory

try:
    UserFactory = importlib.import_module(
        "app.core.factories.user_factories"
    ).UserFactory
except (ImportError, AttributeError):
    UserFactory = None


class PaymentFactory(DjangoModelFactory):
    class Meta:
        model = apps.get_model("orders.Payment")
        skip_postgeneration_save = True

    user = factory.SubFactory(UserFactory)
    amount = factory.Faker("random_int", min=1000, max=1000000)
    tax = factory.Faker("random_int", min=0, max=10000)
    total_amount = factory.LazyAttribute(lambda obj: obj.amount + obj.tax)
    payment_at = factory.Faker("date_time_this_decade", tzinfo=pytz.UTC)

    user_country_code = factory.Faker("country_code")
    user_email = factory.LazyAttribute(lambda obj: obj.user.email)
    user_name = factory.LazyAttribute(lambda obj: obj.user.name)
    user_post_code = factory.LazyAttribute(lambda obj: obj.user.post_code)
    user_prefecture = factory.LazyAttribute(lambda obj: obj.user.prefecture)
    user_address1 = factory.LazyAttribute(lambda obj: obj.user.address1)
    user_address2 = factory.LazyAttribute(lambda obj: obj.user.address2)
    user_tel1 = factory.Faker("numerify", text="080-####-####")
    user_tel2 = factory.Faker("numerify", text="080-####-####")

    company_country_code = factory.Faker("country_code")
    company_name = factory.Faker("company")
    company_post_code = factory.Faker("postcode")
    company_prefecture = factory.Faker("state")
    company_address1 = factory.Faker("street_address")
    company_address2 = factory.Faker("secondary_address")
    company_tel1 = factory.Faker("numerify", text="080-####-####")
    company_tel2 = factory.Faker("numerify", text="080-####-####")
    stripe_code = factory.Sequence(lambda n: f"stripe_{n}_{random.randint(1000, 9999)}")
