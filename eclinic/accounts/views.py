from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm
from clinicians.forms import ClinicianForm
from patients.forms import PatientForm
from patients.models import Patient
from clinicians.models import Clinician
from django.contrib.auth.forms import AuthenticationForm

# Choose Role Page (fallback if user has no role yet)
@login_required
def choose_role(request):
    if hasattr(request.user, 'clinician'):
        return redirect('clinician_dashboard')
    elif hasattr(request.user, 'patient'):
        return redirect('patient_dashboard')
    return render(request, 'accounts/choose_role.html')

# Patient Signup
def patient_signup(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        patient_form = PatientForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.save()
            login(request, user)
            return redirect('patient_dashboard')
    else:
        user_form = UserSignupForm()
        patient_form = PatientForm()
    return render(request, 'accounts/patient_signup.html', {
        'user_form': user_form, 
        'patient_form': patient_form
    })

# Clinician Signup
def clinician_signup(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        clinician_form = ClinicianForm(request.POST)
        if user_form.is_valid() and clinician_form.is_valid():
            user = user_form.save()
            clinician = clinician_form.save(commit=False)
            clinician.user = user
            clinician.save()
            login(request, user)
            return redirect('clinician_dashboard')
    else:
        user_form = UserSignupForm()
        clinician_form = ClinicianForm()
    return render(request, 'accounts/clinician_signup.html', {
        'user_form': user_form, 
        'clinician_form': clinician_form
    })

# Login View (redirects based on role)
def login_view(request):
             # Auto-redirect if already logged in
    if request.user.is_authenticated:
        if hasattr(request.user, 'patient'):
            return redirect('patient_dashboard')
        if hasattr(request.user, 'clinician'):
            return redirect('clinician_dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)


            # Redirect based on role
            if hasattr(user, 'clinician'):
                return redirect('clinician_dashboard')
            elif hasattr(user, 'patient'):
                return redirect('patient_dashboard')
            else:
                return redirect('choose_role')  # fallback if no role
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def home(request):
    return render(request, 'accounts/home.html')

# Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
