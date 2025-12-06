from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('choose-role/', views.choose_role, name='choose_role'),
    path('signup/patient/', views.patient_signup, name='patient_signup'),
    path('signup/clinician/', views.clinician_signup, name='clinician_signup'),
    path('home', views.home, name='home'),
    path('mpesaPayment/', views.mpesaPayment, name='mpesaPayment'),
    ]