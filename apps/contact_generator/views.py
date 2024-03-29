from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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


class ContactCreateView(CreateView):
    model = Contact
    fields = (
        "name",
        "number",
        "is_auto_generated",
    )
    success_url = reverse_lazy("contacts:list_by_class")


class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        "id",
        "name",
        "number",
        "is_auto_generated",
    )
    success_url = reverse_lazy("contacts:list_by_class")


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy("contacts:list_by_class")
