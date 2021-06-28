from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Product)

class ScanAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Scan, ScanAdmin)
