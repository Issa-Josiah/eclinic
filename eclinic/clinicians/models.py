from django.db import models
from django.contrib.auth.models import User

class Clinician(models.Model):
    SPECIALIZATIONS = (
        ('general', 'General Doctor'),
        ('dentist', 'Dentist'),
        ('pediatric', 'Pediatrician'),
        ('cardiology', 'Cardiologist'),
        ('dermatology', 'Dermatologist'),
        ('other', 'Other'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATIONS)
    on_duty = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} ({self.specialization})"

'''
from django.db import models
from accounts.models import User

# Create your models here.

class Clinician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    
    DUTY_CHOICES = (
        ('on', 'On Duty'),
        ('off', 'Off Duty'),
    )
    duty_status = models.CharField(max_length=10, choices=DUTY_CHOICES, default='off')

    def __str__(self):
        return f"{self.user.username} – {self.specialization} ({self.duty_status})"
'''