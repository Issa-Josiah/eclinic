from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClinicianForm
from .models import Clinician
from accounts.decorators import clinician_required


@clinician_required
def clinician_profile(request):
    clinician = get_object_or_404(Clinician, user=request.user)

    if request.method == 'POST':
        form = ClinicianForm(request.POST, instance=clinician)
        if form.is_valid():
            form.save()
            return redirect('clinician_dashboard')  # redirect to profile after saving
    else:
        form = ClinicianForm(instance=clinician)

    return render(request, 'clinicians/clinician_profile.html', {'form': form})
