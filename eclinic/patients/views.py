from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import Patient
from django.contrib.auth.decorators import login_required
from accounts.decorators import patient_required


@login_required
@patient_required
def patient_profile(request):
    patient = Patient.objects.get(user=request.user)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_dashboard')
    else:
        form = PatientForm(instance=patient)

    return render(request, 'patients/patient_profile.html', {'form': form})
