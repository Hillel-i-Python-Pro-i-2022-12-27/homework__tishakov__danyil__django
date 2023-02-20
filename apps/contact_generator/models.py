from django.db import models
from phone_field import PhoneField


class Contact(models.Model):
    name = models.CharField(max_length=50)
    number = PhoneField(blank=True, help_text="Contact phone number")

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_auto_generated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.name}-{self.number}'

    __repr__ = __str__
