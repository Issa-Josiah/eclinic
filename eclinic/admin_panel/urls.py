from django.urls import path
from . import views

urlpatterns = [
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),

    # PATIENTS
    path("patients/", views.manage_patients, name="manage_patients"),
    path("patients/add/", views.add_patient, name="add_patient"),
    path("patients/edit/<int:pk>/", views.edit_patient, name="edit_patient"),

    # CLINICIANS
    path("clinicians/", views.manage_clinicians, name="manage_clinicians"),
    path("clinicians/update_status/<int:pk>/", views.update_clinician_status, name="update_clinician_status"),
    path("clinicians/add/", views.add_clinician, name="add_clinician"),
    path("clinicians/edit/<int:pk>/", views.edit_clinician, name="edit_clinician"),

    # APPOINTMENTS
    path("appointments/", views.manage_appointments, name="manage_appointments"),
    path("appointments/edit/<int:pk>/", views.edit_appointment, name="edit_appointment"),
]
