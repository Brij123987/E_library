from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from addcart.models import CartItem
from book.models import Comic, Magazine
from itertools import zip_longest
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def add_comic_to_cart(request, comic_id):
    user = request.user
    content_type = ContentType.objects.get_for_model(Comic)
    comic = Comic.objects.get(pk=comic_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=user,
        content_type=content_type,
        object_id=comic.id,
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('addcart:view_cart')

def add_magazine_to_cart(request, magazine_id):
    user = request.user

    content_type = ContentType.objects.get_for_model(Magazine)
    magazine = Magazine.objects.get(pk=magazine_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=user,
        content_type=content_type,
        object_id=magazine.id
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('addcart:view_cart')


def remove_comic_from_cart(request, comic_id):
    user = request.user
    content_type = ContentType.objects.get_for_model(Comic)
    CartItem.objects.filter(user=user, content_type=content_type, object_id=comic_id).delete()
    return redirect('addcart:view_cart')

def remove_magazine_from_cart(request, magazine_id):
    user = request.user
    content_type = ContentType.objects.get_for_model(Magazine)
    CartItem.objects.filter(user=user, content_type=content_type, object_id=magazine_id).delete()
    return redirect('addcart:view_cart')


@ login_required
def view_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    cartitem = CartItem.objects.all()
    content_type = ContentType.objects.get_for_model(Comic)
 
    
    item_images = []
    item_names = []
    item_prices = []
    item_id = []
    item_content_type = []

    for cart_item in cart_items:
        content_object = cart_item.content_object

        if isinstance(content_object, Comic):
            item_id.append(content_object.id)
            item_images.append(content_object.comic_image)
            item_names.append(content_object.comic_name)
            item_prices.append(content_object.comic_price)
            item_content_type.append(content_object.model_name)

            
        elif isinstance(content_object, Magazine):
            item_id.append(content_object.id)
            item_images.append(content_object.magazine_image)
            item_names.append(content_object.magazine_name)
            item_prices.append(content_object.magazine_price)
            item_content_type.append(content_object.model_name)

    
    total_price = 0
    for i in item_prices:
        total_price += i


    item_data = list(zip_longest(item_images, item_names, item_prices, item_id, item_content_type, fillvalue=None))
    request.session['item_data'] = item_data

    request.session['total_price'] = total_price
    
    context = {
        'cart_items': cart_items,
        'item_data': item_data,
        'cartitem': cartitem,
        'content_type':content_type,
        'total_price':total_price,
    }
    
    return render(request, 'addcart/view_cart.html', context)