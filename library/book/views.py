from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1 style="color:Grey">This is a book Shelf</h1>')

def detail(request):
    return HttpResponse('<h1 style="color:Blue">This is a Detail Page</h1>')
