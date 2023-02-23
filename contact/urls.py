from django.urls import path
from .views import contact_form

urlpatterns = [
    path('contact/', contact_form, name='contact'),
    #path('contact/success/', contact_success, name='contact_success'),
]
