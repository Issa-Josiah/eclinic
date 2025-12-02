from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

from clinicians.models import Clinician
from patients.models import Patient

@receiver(post_save, sender=User)
def create_related_profile(sender, instance, created, **kwargs):
    if created:
        # Create Profile for every user
        profile = Profile.objects.create(user=instance)

@receiver(post_save, sender=Profile)
def create_user_role_models(sender, instance, created, **kwargs):
    if created:
        # If user is clinician → create clinician model
        if instance.role == 'clinician':
            Clinician.objects.create(user=instance.user)

        # If user is patient → create patient model
        if instance.role == 'patient':
            Patient.objects.create(user=instance.user)
            
'''
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
'''
