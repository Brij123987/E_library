from django.shortcuts import render, redirect
from checkout.models import Checkout_Detail
from checkout.forms import Checkout_Forms
from django.http import JsonResponse
import json
import datetime
from checkout.models import Transaction
from django.contrib import messages
from book.models import Comic, Magazine
from addcart.models import CartItem




# Create your views here.

# Cumtomers Details -----------------------------

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


# Payment Page --------------------------

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


# Paypal Integration ------------------------------


def OnApprove(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            status = body.get('status', None)

            if status == 'COMPLETED':
                trans_id = body.get('transID', None)
                payment_method = body.get('payment_method', None)

                new_transaction = Transaction.objects.create(
                    trans_id=trans_id,
                    status=status,
                    payment_method=payment_method,
                    user = request.user
                )

                request.session['trans_id'] = new_transaction.trans_id

                # Get the user's cart items
                user = request.user
                cart_items = CartItem.objects.filter(user=user)

                # Loop through cart items and associate with the transaction
                for cart_item in cart_items:
                    cart_item.user == request.user
                    cart_item.save()
                    content_object = cart_item.content_object
                    if isinstance(content_object, Comic):
                            content_object.transaction = new_transaction
                            content_object.save()
                    elif isinstance(content_object, Magazine):
                            content_object.transaction = new_transaction
                            content_object.save()

                messages.success(request, 'Payment successful. Your items are now associated with the transaction.')

        except Exception as e:
            messages.error(request, f'Error processing payment: {str(e)}')

        context = {

        }
        # Redirect to the 'checkout:paymentsuccess' page regardless of success or failure
        return JsonResponse(context)
    

# Payment Success Page -------------------------------

def PaymentSuccess(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)

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

    trans_id = request.session.get('trans_id')
     

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
        'trans_id':trans_id
    }

    cart_items.delete()

    return render(request, 'checkout/paymentsuccess.html', context)



