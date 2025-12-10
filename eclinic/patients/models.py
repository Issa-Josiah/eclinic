from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, default='Unknown Patient')
    phone_number = models.CharField(max_length=20, blank=True)
    age = models.IntegerField(null=True, blank=True)
    medical_history = models.TextField(blank=True)
    dob = models.DateField(null=True, blank=True)  # Added date of birth
    emergency_contact = models.CharField(max_length=50, blank=True)  # Added emergency contact

    def __str__(self):
        return self.full_name
