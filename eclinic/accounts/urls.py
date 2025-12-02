from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard_redirect_view, name='dashboard'),
    
    path('dashboard/patient/', views.patient_dashboard_view, name='patient_dashboard'),
    path('dashboard/clinician/', views.clinician_dashboard_view, name='clinician_dashboard'),
    path('dashboard/admin/', views.admin_dashboard_view, name='admin_dashboard'),
]
