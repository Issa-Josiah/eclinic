from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test

from clinicians.models import Clinician
from patients.models import Patient
from appointments.models import Appointment

from .forms import ClinicianForm, PatientForm, AppointmentForm

# Check if user is admin
def is_admin(user):
    return user.is_superuser

# ----------------------
# DASHBOARD
# ----------------------
@user_passes_test(is_admin)
def admin_dashboard(request):
    context = {
        "total_patients": Patient.objects.count(),
        "total_clinicians": Clinician.objects.count(),
        "total_appointments": Appointment.objects.count(),
        "active_appointments": Appointment.objects.filter(status="Pending").count(),
    }
    return render(request, "admin_panel/admin_dashboard.html", context)

# ----------------------
# PATIENT MANAGEMENT
# ----------------------
@user_passes_test(is_admin)
def manage_patients(request):
    patients = Patient.objects.all()
    return render(request, "admin_panel/patient.html", {"patients": patients})

@user_passes_test(is_admin)
def add_patient(request):
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("manage_patients")
    return render(request, "admin_panel/form.html", {"form": form, "title": "Add Patient"})

@user_passes_test(is_admin)
def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        return redirect("manage_patients")
    return render(request, "admin_panel/form.html", {"form": form, "title": "Edit Patient"})

# ----------------------
# CLINICIAN MANAGEMENT
# ----------------------
@user_passes_test(is_admin)
def manage_clinicians(request):
    clinicians = Clinician.objects.all()
    return render(request, "admin_panel/clinician.html", {"clinicians": clinicians})

@user_passes_test(is_admin)
def update_clinician_status(request, pk):
    clinician = get_object_or_404(Clinician, pk=pk)
    clinician.duty_status = 'Off Duty' if clinician.duty_status == 'On Duty' else 'On Duty'
    clinician.save()
    return redirect('manage_clinicians')

@user_passes_test(is_admin)
def add_clinician(request):
    form = ClinicianForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("manage_clinicians")
    return render(request, "admin_panel/form.html", {"form": form, "title": "Add Clinician"})

@user_passes_test(is_admin)
def edit_clinician(request, pk):
    clinician = get_object_or_404(Clinician, pk=pk)
    form = ClinicianForm(request.POST or None, instance=clinician)
    if form.is_valid():
        form.save()
        return redirect("manage_clinicians")
    return render(request, "admin_panel/form.html", {"form": form, "title": "Edit Clinician"})

# ----------------------
# APPOINTMENT MANAGEMENT
# ----------------------
@user_passes_test(is_admin)
def manage_appointments(request):
    appointments = Appointment.objects.all().order_by("-date", "-time")
    return render(request, "admin_panel/appointments.html", {"appointments": appointments})

@user_passes_test(is_admin)
def edit_appointment(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    form = AppointmentForm(request.POST or None, instance=appt)
    if form.is_valid():
        form.save()
        return redirect("manage_appointments")
    return render(request, "admin_panel/form.html", {"form": form, "title": "Edit Appointment"})
