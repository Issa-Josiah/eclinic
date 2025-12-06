from django.shortcuts import render, redirect
from django import forms
from .models import Appointment
from patients.models import Patient
from clinicians.models import Clinician
from accounts.decorators import patient_required, clinician_required
from appointments.models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['clinician', 'date', 'time', 'reason']

# Patient books an appointment
@patient_required
def book_appointment(request):
    patient = Patient.objects.get(user=request.user)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.save()
            return redirect('patient_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})

# List appointments for patient
@patient_required
def patient_appointments(request):
    try:
        patient = Patient.objects.get(user=request.user)
    except Patient.DoesNotExist:
        patient = None

    appointments = Appointment.objects.filter(patient=patient) if patient else []

    context = {
        'appointments': appointments,
        'is_patient': bool(patient),
        'is_clinician': hasattr(request.user, 'clinician'),

    }

    return render(request, 'appointments/appointments_list.html', context)

# List appointments for clinician
@clinician_required
def clinician_appointments(request):
    clinician = Clinician.objects.get(user=request.user)
    appointments = Appointment.objects.filter(clinician=clinician)
    return render(request, 'appointments/appointments_list.html', {'appointments': appointments})


@patient_required
def patient_dashboard(request):
    patient = Patient.objects.get(user=request.user)
    appointments = Appointment.objects.filter(patient=patient).order_by('-date', '-time')[:5]
    return render(request, 'dashboard/patient_dashboard.html', {
        'appointments': appointments
    })

@clinician_required
def clinician_dashboard(request):
    clinician = Clinician.objects.get(user=request.user)
    appointments = Appointment.objects.filter(clinician=clinician).order_by('date', 'time')[:5]
    return render(request, 'dashboard/clinician_dashboard.html', {
        'appointments': appointments
    })

