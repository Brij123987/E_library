from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import logout


# Create your views here.


# Forget Password ---------------

class CustomPasswordResetView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registration/password_rest_form.html'
    email_template_name = 'registration/password_rest_email.html'
    subject_template_name = 'registration/password_rest_subject.txt'
    success_message = "Password reset email has been sent successfully."
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        # Check if the email exists in your system
        if not user_exists_with_email(email):
            messages.info(self.request, 'This email address does not exist.')
            return self.form_invalid(form)
        return super().form_valid(form)


def user_exists_with_email(email):
    return User.objects.filter(email=email).exists()
    

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_rest_confirm.html'
    success_url = reverse_lazy('registration:password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_rest_complete.html'


# Change Password -----------------
    
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            logout(request)  # Log the user out after changing the password
            messages.success(request, f'Congratulations, your password has been changed successfully. Please log in again.')
            return redirect('users:login')
        
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})

