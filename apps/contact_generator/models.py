from django.db import models
from phone_field import PhoneField


class Nationality(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    __repr__ = __str__


class Contact(models.Model):
    name = models.CharField(max_length=50)
    number = PhoneField(blank=True, help_text="Contact phone number")

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_auto_generated = models.BooleanField(default=False)

    avatar = models.ImageField(
        max_length=255,
        upload_to="contact/avatar",
        blank=True,
        null=True,
    )

    nationality = models.ForeignKey(
        Nationality,
        on_delete=models.CASCADE,
        related_name="nationality",
        default=None,
        null=True,
        blank=False,
    )

    def __str__(self) -> str:
        return f"{self.name}-{self.number}"

    __repr__ = __str__
