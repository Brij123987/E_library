from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from book.models import Newspaper
from book.models import Magazine
from book.models import Comic
from book.models import TimesofIndia, HindustanTime, IndianExpress, IndiaToday
from book.forms import UploadTimesofIndiaNewspaper,NewspaperForm, MagazineForm, ComicForm, ContactForm
from book.forms import UploadHindustanNewspaper, UploadIndianExpressNewspaper, UploadIndiaTodayNewspaper
from addcart.models import CartItem
from book.forms import UploadComicPdf, UploadMagazinePdf
import os


# Create your views here.

# Function based index view
# ------------------------------------------------------------------------------------------------


def index(request):
    itemlist = Newspaper.objects.all()

    context = {
        'itemlist':itemlist
    }

    return render(request, 'book/index.html', context)


# Function based magazine view
# ------------------------------------------------------------------------------------------------


def magazine(request):
    magazinelist = Magazine.objects.all()

    context = {
        'magazinelist':magazinelist
    }

    return render(request, 'book/magazine.html', context)


# Function based comic view
# ------------------------------------------------------------------------------------------------


def comic(request):
    comiclist = Comic.objects.all()

    context = {
        'comiclist':comiclist
    }

    return render(request, 'book/comic.html', context)


# Function based detail view
# ------------------------------------------------------------------------------------------------


def detail(request, item_id):
    item = Newspaper.objects.get(pk = item_id)

    context ={
        'item':item
    }
    return render (request, 'book/detail.html', context)


# Function based detail_m view
# ------------------------------------------------------------------------------------------------


def detail_m(request, magazine_id):
    magazine = Magazine.objects.get(pk = magazine_id)

    context = {
        'magazine':magazine
    }

    return render(request, 'book/detail_m.html', context)


# Function based detail_c view
# ------------------------------------------------------------------------------------------------


def detail_c(request, comic_id):
    comic = Comic.objects.get(pk = comic_id)

    context = {
        'comic':comic
    }

    return render(request, 'book/detail_c.html', context)


# Function based Create view
# ------------------------------------------------------------------------------------------------


def create_item(request):
    form = NewspaperForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('book:index')
      
    context = {
        'form':form
    }

    return render(request, 'book/item-form.html', context)


# Function based Create_magazine view
# ------------------------------------------------------------------------------------------------


def create_magazine(request):
    form_1 = MagazineForm(request.POST or None)

    if form_1.is_valid():
        form_1.save()
        return redirect('book:magazine')
    
    context = {
        'form_1':form_1
    }

    return render(request, 'book/magazine-form.html', context)


# Function based Create_comic view
# ------------------------------------------------------------------------------------------------


def create_comic(request):
    form_2 = ComicForm(request.POST or None)

    if form_2.is_valid():
        form_2.save()
        return redirect('book:comic')
    
    context = {
        'form_2':form_2
    }

    return render(request, 'book/comic-form.html', context)

    
# Function based Update view
# ------------------------------------------------------------------------------------------------


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


# Function based Update_magazine view
# ------------------------------------------------------------------------------------------------


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


# Function based Update_comic view
# ------------------------------------------------------------------------------------------------


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



# Function based delete view
# ------------------------------------------------------------------------------------------------


def delete_item(request, item_id):
    item = Newspaper.objects.get(pk = item_id)

    context = {
        'item':item
    }

    if request.method == 'POST':
        item.delete()
        return redirect('book:index')
    
    return render(request, 'book/delete-item.html', context)


# Function based delete_magazine view
# ------------------------------------------------------------------------------------------------

def delete_magazine(request, magazine_id):
    magazine = Magazine.objects.get(pk = magazine_id)

    context = {
        'magazine':magazine
    }

    if request.method == 'POST':
        magazine.delete()
        return redirect('book:magazine')

    return render(request, 'book/delete-magazine.html', context)


# Function based delete_comic view
# ------------------------------------------------------------------------------------------------


def delete_comic(request, comic_id):
    comic = Comic.objects.get(pk = comic_id)

    context = {
        'comic':comic
    }

    if request.method == "POST":
        comic.delete()
        return redirect('book:comic')
    
    return render(request, 'book/delete-comic.html', context)


# Function based contact view
# ------------------------------------------------------------------------------------------------


def send_email(request):
    contact_form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
            subject = 'E-Library: (Feedback Email)'
            message = f'You have received a new Feedback Email. Details:\n\n{contact_form.cleaned_data}'
            form_email = settings.EMAIL_HOST_USER
            recipient_list = ['brijeshyadav9811@gmail.com']

            send_mail(subject, message, form_email, recipient_list, fail_silently=False)

            return redirect('book:index')

    context = {
        'contact_form': contact_form
    }

    return render(request, 'book/contact_form.html', context)



# Function based book_upload view
# ------------------------------------------------------------------------------------------------


def BookUploadView(request, detail_id):
    item = Newspaper.objects.get(pk=detail_id)
    if request.method == 'POST':
        if item.id == 1:
            form = UploadTimesofIndiaNewspaper(request.POST, request.FILES)

            if form.is_valid():
                form.save()
            return redirect('book:index')
        
        elif item.id == 2:
            form = UploadHindustanNewspaper(request.POST, request.FILES)

            if form.is_valid():
                form.save()
            return redirect('book:index')
        
        elif item.id == 3:
            form = UploadIndianExpressNewspaper(request.POST, request.FILES)

            if form.is_valid():
                form.save()
            return redirect('book:index')
        
        elif item.id == 4:
            form = UploadIndiaTodayNewspaper(request.POST, request.FILES)

            if form.is_valid():
                form.save()
            return redirect('book:index')
    

    else:
        if item.id == 1:
            form = UploadTimesofIndiaNewspaper()
        elif item.id == 2:
            form = UploadHindustanNewspaper()
        elif item.id == 3:
            form = UploadIndianExpressNewspaper()
        elif item.id == 4:
            form = UploadIndiaTodayNewspaper()

        context = {
            'form':form,
            'item': item
        }

    return render(request, 'book/uploadbook.html', context)



def news_views(request, item_id):
    news = TimesofIndia.objects.all()
    hind = HindustanTime.objects.all()
    express = IndianExpress.objects.all()
    today = IndiaToday.objects.all()
    news_id = Newspaper.objects.get(pk=item_id)

    context = {
        'news': news,
        'hind': hind,
        'express': express,
        'today': today,
        'news_id': news_id
    }

    return render (request, 'book/news.html', context)


def delete_news(request,news_id,delete_id):
    news = Newspaper.objects.get(pk = news_id)
    if news.id == 1:
        news_delete = TimesofIndia.objects.get(pk=delete_id)

        context = {
            'news_delete':news_delete,
            'news':news
        }

        if request.method == 'POST':
            news_delete.delete()
            return redirect('book:index')
        
        return render(request, 'book/delete_news.html', context)

    elif news.id == 2:
        hind_delete = HindustanTime.objects.get(pk=delete_id)

        context = {
            'hind_delete':hind_delete,
            'news':news
        } 

        if request.method == 'POST':
            hind_delete.delete()
            return redirect('book:index')

        return render(request, 'book/delete_news.html', context)
    
    elif news.id == 3:
        express_delete = IndianExpress.objects.get(pk=delete_id)

        context = {
            'express_delete':express_delete,
            'news':news
        }

        if request.method == 'POST':
            express_delete.delete()
            return redirect('book:index')
        
        return render(request,'book/delete_news.html',context)
    
    elif news.id == 4:
        today_delete = IndiaToday.objects.get(pk = delete_id)

        context = {
            'today_delete':today_delete,
            'news':news
        }

        if request.method == 'POST':
            today_delete.delete()
            return redirect('book:index')
        
        return render(request,'book/delete_news.html',context)
    
def Upload_Comic_Magazine(request, detail_id):
    cartitem = CartItem.objects.all()
    for cart_item in cartitem:
        content_object = cart_item.content_object

        if isinstance(content_object, Comic):
            item = Comic.objects.get(pk = detail_id)
            if request.method == 'POST':
                form = UploadComicPdf(request.POST, request.FILES)

                if form.is_valid():
                    form.save()
                    return redirect('book:comic')
            
            else:
                form = UploadComicPdf()

                context = {
                    'item':item,
                    'form':form
                }

            return render(request,'book/uploadComicMagazine.html',context)
        
        elif isinstance(content_object, Magazine):
            item = Magazine.objects.get(pk = detail_id)
            if request.method == 'POST':
                form = UploadMagazinePdf(request.POST, request.FILES)

                if form.is_valid():
                    form.save()
                    return redirect('book:magazine')
            
            else:
                form = UploadMagazinePdf()

                context = {
                    'item':item,
                    'form':form
                }

            return render(request,'book/uploadComicMagazine.html',context)








