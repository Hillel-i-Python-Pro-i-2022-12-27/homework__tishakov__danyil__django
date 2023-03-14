from django.contrib.auth.models import (
    AbstractUser,
)


class User(AbstractUser):
    pass


# no


# class MyUserManager(BaseUserManager):
#     def _create_user(self, username, email, password, **extra_fields):
#         if not email:
#             raise ValueError("Input your email")
#         if not username:
#             raise ValueError("Input your username")
#         user = self.model(email=self.normalize_email(email), username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
