from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient
from clinicians.models import Clinician

class Appointment(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    clinician = models.ForeignKey(Clinician, on_delete=models.CASCADE)

    date = models.DateField()
    time = models.TimeField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.user.username} → {self.clinician.user.username} on {self.date}"

'''
from django.db import models
from patients.models import Patient
from clinicians.models import Clinician

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    clinician = models.ForeignKey(Clinician, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.patient} with {self.clinician} on {self.date} at {self.time}"
'''

