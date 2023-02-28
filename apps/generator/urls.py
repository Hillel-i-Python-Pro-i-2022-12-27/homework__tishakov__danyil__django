from django.urls import path

from apps.generator import views

app_name = "generator"

urlpatterns = [
    path("user/", views.index, name="index"),
    path("", views.home_page, name="home_page"),
]
