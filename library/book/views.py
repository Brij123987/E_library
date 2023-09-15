from django.shortcuts import render
from django.http import HttpResponse
from book.models import Newspaper
from book.models import Magazine
from book.models import Comic


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
    return HttpResponse(f'item_id:{item_id}')
