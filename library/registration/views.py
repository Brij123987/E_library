from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


# Create your views here.

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_rest_form.html'
    email_template_name = 'registration/password_rest_email.html'
    subject_template_name = 'registration/password_rest_subject.txt'
    success_url = reverse_lazy('users:login')
    

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_rest_confirm.html'
    success_url = reverse_lazy('registration:password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_rest_complete.html'


# Change Password
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, f'Congratulation, your password has been changed successfully, Now you can login again.')
            return redirect('users:login')
        
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form':form})

