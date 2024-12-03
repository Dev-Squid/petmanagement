from django.contrib import admin
from . import models

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'paided_customer', 'validated', 'created_at', 'updated_at')
    list_filter = ('paided_customer', 'validated', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone_number')
    list_per_page = 25

admin.site.register(models.Allergy)