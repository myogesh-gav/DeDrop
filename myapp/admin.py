from django.contrib import admin
from .models import *

# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_display = ['addressof','country']
    
    class Meta:
        js = ("myapp/selectajax.js",)

admin.site.register(Address,AddressAdmin)
admin.site.register([Country,Division,District,SubDistrict])