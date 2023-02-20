import typing

from faker import Faker

from apps.contact_generator import models


def generate_of_contacts(
        amount: int = 100,
        is_auto_generated: bool = False
) -> typing.Iterator[models.Contact]:
    fake = Faker()
    for _ in range(amount):
        yield models.Contact(
            name=fake.name(),
            number=fake.phone_number(),
            is_auto_generated=is_auto_generated,
        )
