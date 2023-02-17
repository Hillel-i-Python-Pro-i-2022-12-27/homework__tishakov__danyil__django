from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_auto_generated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.name}-{self.number}'

    __repr__ = __str__

    # @classmethod
    # def generate_of_contacts(amount: int = 10):
    #     from faker import Faker
    #     fake = Faker
    #     for _ in range(amount):
    #         yield models.Contact(
    #             name=fake.name(),
    #             number=fake.phone_number(),
    #         )



