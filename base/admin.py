from django.contrib import admin

# Register your models here.

from .models import ContactMessage

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email','created_at')



admin.site.register(ContactMessage, MyModelAdmin)
