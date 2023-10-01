from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import RegisterForm
from django.contrib.auth import login,logout, authenticate

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, you account have been successfully created')
            form.save()
            return redirect('book:index')
        
    else:
        form = RegisterForm()

        context ={ 
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
            return redirect('book:index')
        

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('users:login')

