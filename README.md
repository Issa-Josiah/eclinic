# eClinic – Role-Based Medical Appointment System

A lightweight digital clinic system, providing a modern appointment-booking platform for patients and clinicians.  
The system offers role-based dashboards, profile management, and appointment handling—ideal for prototyping e-health applications.

---

## Project Purpose

eClinic is designed to simplify healthcare interactions by enabling:

- Easy communication between patients and clinicians  
- Digital booking of medical appointments  
- Role-specific dashboards and profile management  
- Streamlined service delivery without paperwork  
- A clean, expandable architecture suitable for growth into a full EMR (Electronic Medical Records) system  

This project serves as a foundation for more advanced digital health systems.

---

## Main Features

### Authentication & Role Handling
- Signup for patients and clinicians  
- Login using Django’s secure authentication system  
- Automatic redirection after login:
  - Patients → Patient Dashboard  
  - Clinicians → Clinician Dashboard  
- Logout and session management  
- Role protection using custom decorators (`patient_required`, `clinician_required`)  

### Clinician Features
- Clinician signup with personal details  
- Editable clinician profile:
  - Full name  
  - Phone number  
  - Specialization  
  - Duty status  
- Access to their own clinician dashboard  
- View appointments assigned to them  

### Patient Features
- Patient signup with personal information  
- Editable patient profile:
  - Full name  
  - Phone number  
  - Date of birth  
- Patient dashboard with recent appointment overview  
- Book an appointment with available clinicians  
- View all appointments they have booked  

### Appointment Management
- Patients can book appointments by selecting:
  - Clinician  
  - Date  
  - Time  
  - Reason for visit  
- Clinicians can view all appointments involving them  
- Shared appointment list template for cleaner UI  

### Dashboard System
**Patient Dashboard**
- Shows patient details  
- Recent appointments list  
- Quick links to:
  - Update profile  
  - Book appointment  

**Clinician Dashboard**
- Shows clinician details  
- Upcoming appointments list  
- Quick links to:
  - Edit profile  

### Admin Panel
- Using the Django admin interface, administrators can manage:
  - Users  
  - Patients  
  - Clinicians  
  - Appointments  
- This makes debugging, testing, and monitoring easy.

---

## Project Structure

```
eclinic/
│
├── accounts/       → login, signup, logout, role routing
├── clinicians/     → clinician models, forms, views
├── patients/       → patient models, forms, views
├── appointments/   → booking and appointment listing
├── dashboard/      → shared dashboard logic
│
├── eclinic/        → main project config (urls, settings)
├── templates/      → HTML templates for all apps
└── static/         → optional static files (CSS/JS)
```

---

## Technology Stack

- Backend: Django (Python)  
- Frontend: HTML, Django Templates (Bootstrap optional)  
- Database: SQLite (default)  
- Authentication: Django Auth  

---

## Future Enhancements

