import secrets

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from faker import Faker

fake = Faker("en_US")


def home_page(request):
    return render(request=request, template_name="index.html", context={})


def home_page(request):
    return render(request=request,
                  template_name="index.html",
                  context={})


def index(request: WSGIRequest):
    login = fake.first_name().lower()
    email = f"{login}{secrets.token_hex(1)}@gmail.com"
    password = fake.password(7)
    return render(
        request=request,
        template_name="contacts/contacts_list.html",
        context={
            "email": email,
            "login": login,
            "password": password,
        },
    )
