from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone_number', 'age')
    search_fields = ('user__username', 'full_name', 'phone_number')
