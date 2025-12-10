from django import forms
from .models import Appointment
from clinicians.models import Clinician

class AppointmentForm(forms.ModelForm):
    clinician = forms.ModelChoiceField(
        queryset=Clinician.objects.filter(duty_status='On Duty'),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Appointment
        fields = ['clinician', 'date', 'time', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
