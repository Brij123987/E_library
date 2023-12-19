from django.shortcuts import render, redirect
from checkout.models import Checkout_Detail
from checkout.forms import Checkout_Forms


# Create your views here.

def chk_form(request):
    if request.method == 'POST':
        check_form = Checkout_Forms(request.POST)

        if check_form.is_valid():
            check_form.save()
            return redirect('book:index')
    
    else:
        check_form = Checkout_Forms()

        context = {
            'check_form':check_form
        }
    
    return render(request,'checkout/check_page.html',context)

