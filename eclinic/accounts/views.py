from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Profile
from .forms import SignupForm, LoginForm

# -------------------------
# SIGN UP VIEW
# -------------------------
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # signup form already sets password + role
            user.save()
            user._role = form.cleaned_data['role']
            messages.success(request, "Account created successfully!")
            return redirect('login')

    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


# -------------------------
# LOGIN VIEW
# -------------------------
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('dashboard_redirect')  # FIXED
            else:
                messages.error(request, "Invalid username or password")

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


# -------------------------
# LOGOUT
# -------------------------
def logout_view(request):
    logout(request)
    return redirect('login')


# -------------------------
# DASHBOARD REDIRECT BASED ON ROLE
# -------------------------
@login_required
def dashboard_redirect(request):
    role = request.user.profile.role

    if role == "patient":
        return redirect('patient_dashboard')
    elif role == "clinician":
        return redirect('clinician_dashboard')
    elif role == "admin":
        return redirect('admin_dashboard')

    # fallback
    messages.error(request, "Invalid role assigned.")
    return redirect('login')


# -------------------------
# DASHBOARD PAGES
# -------------------------
@login_required
def patient_dashboard_view(request):
    return render(request, 'accounts/patient_dashboard.html')


@login_required
def clinician_dashboard_view(request):
    return render(request, 'accounts/clinician_dashboard.html')


@login_required
def admin_dashboard_view(request):
    return render(request, 'accounts/admin_dashboard.html')
