from django.shortcuts import render, redirect
from accounts.decorators import patient_required, clinician_required
from patients.models import Patient
from clinicians.models import Clinician
from appointments.models import Appointment

# -------------------------------
# Patient Dashboard
# -------------------------------
@patient_required
def patient_dashboard(request):
    patient = Patient.objects.get(user=request.user)
    # Show last 5 upcoming appointments
    appointments = Appointment.objects.filter(patient=patient).order_by('date', 'time')[:5]
    context = {
        'patient': patient,
        'appointments': appointments,
    }
    return render(request, 'dashboard/patient_dashboard.html', context)


# -------------------------------
# Clinician Dashboard
# -------------------------------
@clinician_required
def clinician_dashboard(request):
    clinician = Clinician.objects.get(user=request.user)
    # Show next 5 pending appointments
    appointments = Appointment.objects.filter(clinician=clinician, status='Pending').order_by('date', 'time')[:5]
    context = {
        'clinician': clinician,
        'appointments': appointments,
    }
    return render(request, 'dashboard/clinician_dashboard.html', context)


# -------------------------------
# Admin Dashboard
# -------------------------------
def admin_dashboard(request):
    context = {
        'total_patients': Patient.objects.count(),
        'total_clinicians': Clinician.objects.count(),
        'total_appointments': Appointment.objects.count(),
        'active_appointments': Appointment.objects.filter(status='Pending').count(),
        'patients': Patient.objects.all(),
        'clinicians': Clinician.objects.all(),
        'appointments': Appointment.objects.all(),
    }
    return render(request, 'dashboard/admin_dashboard.html', context)
