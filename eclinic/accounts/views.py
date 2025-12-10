from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .forms import UserSignupForm, LoginForm
from .models import UserProfile
from patients.forms import PatientForm
from clinicians.forms import ClinicianForm
from django_daraja.mpesa.core import MpesaClient

# Home View
def home(request):
    return render(request, 'accounts/home.html')


# Index / Test Mpesa
def index(request):
    cl = MpesaClient()
    phone_number = '0708656009'  # Replace with your test number
    amount = 1
    account_reference = 'eClinic Community'
    transaction_desc = 'Donation towards eClinic'
    callback_url = 'https://api.darajambili.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(str(response))


# Choose Role Page
@login_required
def choose_role(request):
    if hasattr(request.user, 'userprofile'):
        role = request.user.userprofile.role
        if role == 'clinician':
            return redirect('clinician_dashboard')
        elif role == 'patient':
            return redirect('patient_dashboard')
    elif request.user.is_superuser:
        return redirect('admin_dashboard')
    return render(request, 'accounts/choose_role.html')


# Patient Signup
def patient_signup(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        patient_form = PatientForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save()
            # Create UserProfile
            UserProfile.objects.create(user=user, role='patient')
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
            # Create UserProfile
            UserProfile.objects.create(user=user, role='clinician')
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


# Login View
def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('admin_dashboard')
        elif hasattr(request.user, 'userprofile'):
            role = request.user.userprofile.role
            if role == 'patient':
                return redirect('patient_dashboard')
            elif role == 'clinician':
                return redirect('clinician_dashboard')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirect based on role
            if user.is_superuser:
                return redirect('admin_dashboard')
            elif hasattr(user, 'userprofile'):
                role = user.userprofile.role
                if role == 'patient':
                    return redirect('patient_dashboard')
                elif role == 'clinician':
                    return redirect('clinician_dashboard')
            return redirect('choose_role')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


# Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# Mpesa Payment View

def mpesaPayment(request):
    if request.method == 'POST':
        cl = MpesaClient()
        phone_number = request.POST.get('phone_number')
        try:
            amount = int(request.POST.get('amount'))
        except (TypeError, ValueError):
            return HttpResponse("Invalid amount", status=400)
        account_reference = 'eClinic Community'
        transaction_desc = 'Payment towards eClinic services'
        callback_url = 'https://api.darajambili.com/express-payment'
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return HttpResponse(str(response))
    else:
        return render(request, 'accounts/mpesaPayment.html')
