from django.db import models
from patients.models import Patient
from clinicians.models import Clinician

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    clinician = models.ForeignKey(Clinician, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField(default='No reason provided')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        # Use User's full name if available, otherwise username
        patient_name = getattr(self.patient.user, 'get_full_name', lambda: str(self.patient.user))()
        clinician_name = getattr(self.clinician.user, 'get_full_name', lambda: str(self.clinician.user))()
        return f"{patient_name} with {clinician_name} on {self.date} at {self.time}"
