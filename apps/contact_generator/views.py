from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from apps.contact_generator.models import Contact


def list_contacts(request):
    return render(
        request=request,
        template_name="contact_generator/contact_list.html",
        context={
            "object_list": Contact.objects.all(),
        },
    )


class ContactListView(ListView):
    model = Contact
    # queryset = Contact.objects.all().order_by("modified_at")


class ContactDetailView(DetailView):
    model = Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = (
        "id",
        "name",
        "nationality",
        "number",
        "avatar",
    )
    success_url = reverse_lazy("contacts:list_by_class")


class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        "id",
        "name",
        "nationality",
        "number",
        "avatar",
    )
    success_url = reverse_lazy("contacts:list_by_class")


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy("contacts:list_by_class")
