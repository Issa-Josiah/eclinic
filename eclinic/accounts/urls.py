from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('choose-role/', views.choose_role, name='choose_role'),
    path('signup/patient/', views.patient_signup, name='patient_signup'),
    path('signup/clinician/', views.clinician_signup, name='clinician_signup'),
    path('mpesaPayment/', views.mpesaPayment, name='mpesaPayment'),
]
