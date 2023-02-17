from django.shortcuts import render

def list_contacts(request):
    return render(
        request,
        template_name='contacts/contacts_list.html',
        # context_instance={
        #     'contacts': Contact.objects.all()
        # }
    )
