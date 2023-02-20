from django.shortcuts import render

from apps.contact_generator.models import Contact


def list_contacts(request):
    return render(
        request=request,
        template_name='db_view/db_view.html',
        context={
            'contacts': Contact.objects.all(),

        }
    )
