from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('patient/', views.patient_appointments, name='patient_appointments'),
    path('clinician/', views.clinician_appointments, name='clinician_appointments'),
]
