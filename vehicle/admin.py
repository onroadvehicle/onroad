from django.contrib import admin
from vehicle.models import *
# Register your models here.

@admin.register(contact)
class contactadmin(admin.ModelAdmin):
    list_display=('name','email','phone','message',)
@admin.register(services)
class servicesadmin(admin.ModelAdmin):
    pass
@admin.register(faq)
class faqadmin(admin.ModelAdmin):
    pass
@admin.register(gallary)
class gallaryadmin(admin.ModelAdmin):
    pass
@admin.register(blog)
class blogsadmin(admin.ModelAdmin):
    pass
@admin.register(appointment)
class appointmentadmin(admin.ModelAdmin):
    list_display=('name','location','mobile','vehicletype','vehiclenumber','vehicleservices','message',)

