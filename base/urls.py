
from django.contrib import admin
from django.urls import path, include
from .views import contact_form
from . import views

urlpatterns = [
    path('',views.home),
     path('contact/', contact_form, name='contact'),
   
]
