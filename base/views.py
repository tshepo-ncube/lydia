from django.shortcuts import render
from .models import ContactMessage

def contact_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        #lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        contact_message = ContactMessage(name=name, email=email,phone=phone)
        contact_message.save()
        #return redirect('contact_success')

    return render(request, 'contact/template_boot.html')


# Create your views here.

def home(request):
    return render(request,'base/template_boot.html')