from django.contrib import admin
from .models import Register, Contact,Product
# Register your models here.

admin.site.register(Register) 
admin.site.register(Contact)
admin.site.register(Product)