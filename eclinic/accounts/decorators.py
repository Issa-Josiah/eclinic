from django.shortcuts import redirect
from functools import wraps

def patient_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'userprofile') and request.user.userprofile.role == 'patient':
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper

def clinician_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'userprofile') and request.user.userprofile.role == 'clinician':
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper
