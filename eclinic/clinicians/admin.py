from django.contrib import admin
from .models import Clinician

@admin.register(Clinician)
class ClinicianAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'specialization', 'duty_status')
    list_filter = ('specialization', 'duty_status')
    search_fields = ('user__username', 'full_name', 'specialization')

