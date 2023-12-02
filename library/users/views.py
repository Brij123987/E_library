from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import RegisterForm
from django.contrib.auth import login,logout, authenticate
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from users.models import Profile
from django.contrib.auth.decorators import login_required



# Create your views here.

def register(request):
    try:
        if request.method == 'POST':
            form = RegisterForm(request.POST)

            if form.is_valid():
                username = form.cleaned_data.get('username')
                messages.success(
                    request,
                    f'Welcome {username}, your account has been successfully created. Now you may login.'
                )
                form.save()
                return redirect('users:login')
        
        else:
            form = RegisterForm()

            context = {
                'form':form
            }

            return render(request, 'users/register.html', context)
        return HttpResponse(redirect('users:register',context))
    except UnboundLocalError as e:
        messages.warning(request, 'Invalid Password combination. Password must have UpperCase, Lowercase and Special Characters.')
        form = RegisterForm()
        context = {
            'form':form
        }
        return render(request, 'users/register.html', context)





def login_view(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}, you have been successfully logged in.')
            return redirect('book:index')
        

    return render(request, 'users/login.html')

def logout_view(request):
    messages.success(request, f'{request.user.username}, you have successully logged out.')
    logout(request)
    return redirect('users:login')

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')

class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'users/edit_profile.html'
    fields = ['image','address','phone_no']
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        # Handle the image field separately if it has changed.
        if 'image' in form.changed_data:
           pass

        return super().form_valid(form)


