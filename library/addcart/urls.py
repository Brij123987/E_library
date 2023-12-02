from django.urls import path, include
from addcart import views

app_name = 'addcart'

urlpatterns = [
        path('add_comic_to_cart/<int:comic_id>/', views.add_comic_to_cart, name='add_comic_to_cart'),
        
        path('add_magazine_to_cart/<int:magazine_id>/', views.add_magazine_to_cart, name='add_magazine_to_cart'),

        path('remove_comic_from_cart/<int:comic_id>/', views.remove_comic_from_cart, name='remove_comic_from_cart'),

        path('remove_magazine_from_cart/<int:magazine_id>/', views.remove_magazine_from_cart, name='remove_magazine_from_cart'),

        path('view_cart/', views.view_cart, name='view_cart'),
]