from django.shortcuts import render, redirect
from checkout.models import Checkout_Detail
from checkout.forms import Checkout_Forms
from django.http import JsonResponse
import json
import datetime
from checkout.models import Transaction



# Create your views here.

def chk_form(request):
    if request.method == 'POST':
        check_form = Checkout_Forms(request.POST)

        if check_form.is_valid():
            check_form.save()
            return redirect('checkout:check_page')

    else:
        check_form = Checkout_Forms()

    context = {
        'check_form': check_form
    }

    return render(request, 'checkout/check_page.html', context)


def payment_page(request):
    check = Checkout_Detail.objects.all()
    today = datetime.date.today()
    now = datetime.datetime.now()
    time = now.time()
    for val in check:
        name = val.name
        address = val.address
        contact = val.contact_number
        pin = val.pin_code
        order_id = val.order_id
    profile = request.user.email
    item_data = request.session.get('item_data', [])

    total_price = request.session.get('total_price', 0)
    
    
    context = {
        'name':name,
        'address':address,
        'contact':contact,
        'pin':pin,
        'order_id':order_id,
        'profile':profile,
        'item_data':item_data,
        'total_price':total_price,
        'today':today,
        'time':time,
    }

    return render(request, 'checkout/checkout.html', context)



def OnApprove(request):

  if request.method == 'POST':
    body = json.loads(request.body)
    status = body.get('status', None)
    
    if status == 'COMPLETED':
        trans_id = body.get('transID', None)
        payment_method = body.get('payment_method', None)

        new_transaction = Transaction.objects.create(
            trans_id = trans_id,
            status = status,
            payment_method = payment_method
        )

    
    
    context = {
        'trans_id': new_transaction.trans_id,
        'payment_method': new_transaction.payment_method,
        'status': new_transaction.status,
    }

    return JsonResponse(context)



def PaymentSuccess(request):
    check = Checkout_Detail.objects.all()
    today = datetime.date.today()
    now = datetime.datetime.now()
    time = now.time()
    for val in check:
        name = val.name
        address = val.address
        contact = val.contact_number
        pin = val.pin_code
        order_id = val.order_id
    profile = request.user.email
    item_data = request.session.get('item_data', [])

    total_price = request.session.get('total_price', 0)
     
    

    context = {
        'name':name,
        'address':address,
        'contact':contact,
        'pin':pin,
        'order_id':order_id,
        'profile':profile,
        'item_data':item_data,
        'total_price':total_price,
        'today':today,
        'time':time,
    }
    return render(request, 'checkout/paymentsuccess.html', context)
