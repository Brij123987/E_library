from django.shortcuts import render, redirect
from django.http import HttpResponse
from book.models import Newspaper
from book.models import Magazine
from book.models import Comic
from book.forms import NewspaperForm, MagazineForm, ComicForm


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
    form_1 = MagazineForm(request.POST or None)
    form_2 = ComicForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('book:index')
    
    elif form_1.is_valid():
        form_1.save()
        return redirect('book:magazine')
    
    elif form_2.is_valid():
        form_2.save()
        return redirect('book:comic')
    
    context = {
        'form':form,
        'form_1':form_1,  
        'form_2':form_2
    }

    return render(request, 'book/item-form.html', context)
    
