from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.clinician_profile, name='clinician_profile'),
]
