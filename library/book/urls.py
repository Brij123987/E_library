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
    path('add/',views.create_item, name='create_item'),
    path('add_m/',views.create_magazine, name='create_magazine'),
    path('add_c/',views.create_comic, name="create_comic"),
    path('update/<int:item_id>/',views.update_item, name="update_item"),
    path('update_magazine/<int:magazine_id>/',views.update_magazine, name="update_magazine"),
    path('update_comic/<int:comic_id>/',views.update_comic, name="update_comic"),
    path('delete/<int:item_id>/',views.delete_item, name='delete_item'),
    path('delete_magazine/<int:magazine_id>/',views.delete_magazine,name='delete_magazine'),
    path('delete_comic/<int:comic_id>/',views.delete_comic,name='delete_comic'),
    path('contact/',views.contact_view, name='contact'),
]