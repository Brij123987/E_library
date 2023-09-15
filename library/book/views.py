from django.shortcuts import render
from django.http import HttpResponse
from book.models import Newspaper

# Create your views here.

def index(request):
    itemlist = Newspaper.objects.all()

    return HttpResponse(itemlist)

def detail(request):
    return HttpResponse('<h1 style="color:Blue">This is a Detail Page</h1>')
