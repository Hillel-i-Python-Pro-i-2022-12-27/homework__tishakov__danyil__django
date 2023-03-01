from django.urls import path, include

from . import views

app_name = "contacts"

urlpatterns = [
    path(
        "list/",
        include(
            [
                path("by-function/", views.list_contacts, name="list_by_function"),
                path("by-class/", views.ContactListView.as_view(), name="list_by_class"),
            ]
        ),
    ),
    path("create/", views.ContactCreateView.as_view(), name="create"),
    path("update/<int:pk>/", views.ContactUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.ContactDeleteView.as_view(), name="delete"),
]
