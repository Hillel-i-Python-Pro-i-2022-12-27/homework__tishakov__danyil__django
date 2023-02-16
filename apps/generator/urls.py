from django.urls import path

from apps.generator import views

app_name = 'generator'

urlpatterns = [
    path('info', views.index, name="index"),
    ]