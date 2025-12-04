from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from clinicians.models import Clinician
from appointments.models import Appointment
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your views here.

@login_required
def dashboard_redirect(request):
    User.userprofile = request.user.profile
    
    if User.userprofile.role == "admin":
        return redirect("admin_dashboard")

    elif User.userprofile.role == "clinician":
        return redirect("clinician_dashboard")

    elif User.userprofile.role == "patient":
        return redirect("patient_dashboard")

    else:
        messages.error(request, "Your account role is invalid. Contact support.")
        return redirect("login")
    

@login_required
def admin_dashboard(request):
    # Ensure only admin users access this
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to access the admin dashboard.")
        return redirect('dashboard_redirect')

    patients = Patient.objects.all()
    clinicians = Clinician.objects.all()
    appointments = Appointment.objects.all().order_by('-date', '-time')

    context = {
        "patients": patients,
        "clinicians": clinicians,
        "appointments": appointments,
    }
    return render(request, "dashboard/admin_dashboard.html", context)

@login_required
def clinician_dashboard(request):
    """Clinician dashboard showing their info and appointments"""
    try:
        clinician = request.user.clinician
    except Clinician.DoesNotExist:
        messages.error(request, "Clinician profile not found.")
        return redirect("dashboard_redirect")

    appointments = Appointment.objects.filter(clinician=clinician)

    context = {
        "clinician": clinician,
        "appointments": appointments,
    }
    return render(request, "dashboard/clinician_dashboard.html", context)


@login_required
def patient_dashboard(request):
    """Patient dashboard showing profile and appointments"""
    try:
        patient = request.user.patient
    except Patient.DoesNotExist:
        messages.error(request, "Patient profile not found.")
        return redirect("dashboard_redirect")

    appointments = Appointment.objects.filter(patient=patient)

    context = {
        "patient": patient,
        "appointments": appointments,
    }
    return render(request, "dashboard/patient_dashboard.html", context)
