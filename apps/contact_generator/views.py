from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from apps.contact_generator.models import Contact


def list_contacts(request):
    return render(
        request=request,
        template_name="contact_view/contact_view.html",
        context={
            "object_list": Contact.objects.all(),
        },
    )


class ContactListView(ListView):
    model = Contact

class ContactCreateView(CreateView):
    model = Contact
    fields = (
        "name",
        "number",
        "is_auto_generated",
    )
    success_url = reverse_lazy("contacts:list_by_functions")

class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        "id",
    1"name",
        "number",
        "is_auto_generated",
    )
    success_url = reverse_lazy("contacts:list_by_functions")

