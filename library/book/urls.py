from django.urls import path, include
from book import views

app_name = 'book'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('magazine/', views.magazine, name='magazine'),
    path('comic/',views.comic, name='comic'),
    path('detail/<int:item_id>/', views.detail, name='detail'),
    path('detail_m/<int:magazine_id>/',views.detail_m, name='detail_m'),
    path('detail_c/<int:comic_id>/',views.detail_c, name= 'detail_c'),
]