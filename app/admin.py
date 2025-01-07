from django.contrib import admin

# Register your models here.
from .models import siteedit,ContactMessage
admin.site.register(siteedit)
admin.site.register(ContactMessage)