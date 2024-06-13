from django.contrib import admin
from .models import form
# Register your models here.

class form_admin(admin.ModelAdmin):
    list_display = ('first_name','last_name','mail','phone','text')

admin.site.register(form)
