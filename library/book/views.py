from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from book.models import Newspaper
from book.models import Magazine
from book.models import Comic
from book.models import Contact
from book.forms import NewspaperForm, MagazineForm, ComicForm, ContactForm


# Create your views here.

def index(request):
    itemlist = Newspaper.objects.all()

    context = {
        'itemlist':itemlist
    }

    return render(request, 'book/index.html', context)

def magazine(request):
    magazinelist = Magazine.objects.all()

    context = {
        'magazinelist':magazinelist
    }

    return render(request, 'book/magazine.html', context)

def comic(request):
    comiclist = Comic.objects.all()

    context = {
        'comiclist':comiclist
    }

    return render(request, 'book/comic.html', context)

def contact(request):
    contact_list = Contact.objects.all()

    context = {
        'contact_list':contact_list
    }

    return render(request, 'book/base.html', context)

def detail(request, item_id):
    item = Newspaper.objects.get(pk = item_id)

    context ={
        'item':item
    }
    return render (request, 'book/detail.html', context)

def detail_m(request, magazine_id):
    magazine = Magazine.objects.get(pk = magazine_id)

    context = {
        'magazine':magazine
    }

    return render(request, 'book/detail_m.html', context)

def detail_c(request, comic_id):
    comic = Comic.objects.get(pk = comic_id)

    context = {
        'comic':comic
    }

    return render(request, 'book/detail_c.html', context)


def create_item(request):
    form = NewspaperForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('book:index')
      
    context = {
        'form':form
    }

    return render(request, 'book/item-form.html', context)

def create_magazine(request):
    form_1 = MagazineForm(request.POST or None)

    if form_1.is_valid():
        form_1.save()
        return redirect('book:magazine')
    
    context = {
        'form_1':form_1
    }

    return render(request, 'book/magazine-form.html', context)

def create_comic(request):
    form_2 = ComicForm(request.POST or None)

    if form_2.is_valid():
        form_2.save()
        return redirect('book:comic')
    
    context = {
        'form_2':form_2
    }

    return render(request, 'book/comic-form.html', context)
    

def update_item(request, item_id):
    item = Newspaper.objects.get(pk = item_id)
    form = NewspaperForm(request.POST or None, instance=item)


    if form.is_valid():
        form.save()
        return redirect('book:index')
    
    context = {
        'form': form
    }

    return render(request, 'book/item-form.html', context)

def update_magazine(request, magazine_id):
    magazine = Magazine.objects.get(pk = magazine_id)
    form_1 = MagazineForm(request.POST or None, instance=magazine)

    if form_1.is_valid():
        form_1.save()
        return redirect('book:magazine')
    
    context ={
        'form_1': form_1
    }

    return render(request, 'book/magazine-form.html', context)

def update_comic(request, comic_id):
    comic = Comic.objects.get(pk = comic_id)
    form_2 = ComicForm(request.POST or None, instance=comic)

    if form_2.is_valid():
        form_2.save()
        return redirect('book:comic')
    
    context ={
        'form_2': form_2
    }

    return render(request, 'book/comic-form.html', context)

def delete_item(request, item_id):
    item = Newspaper.objects.get(pk = item_id)

    context = {
        'item':item
    }

    if request.method == 'POST':
        item.delete()
        return redirect('book:index')
    
    return render(request, 'book/delete-item.html', context)

def delete_magazine(request, magazine_id):
    magazine = Magazine.objects.get(pk = magazine_id)

    context = {
        'magazine':magazine
    }

    if request.method == 'POST':
        magazine.delete()
        return redirect('book:magazine')

    return render(request, 'book/delete-magazine.html', context)

def delete_comic(request, comic_id):
    comic = Comic.objects.get(pk = comic_id)

    context = {
        'comic':comic
    }

    if request.method == "POST":
        comic.delete()
        return redirect('book:comic')
    
    return render(request, 'book/delete-comic.html', context)


def contact_view(request):
    if request.method == 'POST':
        contact_1 = ContactForm(request.POST or None)
        if contact_1.is_valid():
            contact_1.save()

            email_subject = f'New contact {contact_1.cleaned_data["email"]}: {contact_1.cleaned_data["subject"]}'
            
            email_message = contact_1.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            return render(request, 'book/index.html')
        
    contact_1 = ContactForm()
    context = {
        'contact_1': contact_1
    }
    return render(request, 'book/base.html', context)
