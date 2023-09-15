from django.urls import path, include
from book import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('magazine/', views.magazine, name='magazine'),
    path('comic/',views.comic, name='comic'),
    path('detail/', views.detail, name='detail'),
]