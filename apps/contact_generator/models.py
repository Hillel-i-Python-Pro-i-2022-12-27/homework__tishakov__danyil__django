from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    number = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = self.name

    def __str__(self) -> str:
        return f'{self.name}-{self.number}'

    __repr__ = __str__
