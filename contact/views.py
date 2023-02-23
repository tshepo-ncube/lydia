from django.shortcuts import render, redirect
from .models import ContactMessage

def contact_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        contact_message = ContactMessage(name=name, email=email)
        contact_message.save()
        #return redirect('contact_success')

    return render(request, 'contact/template_boot.html')
