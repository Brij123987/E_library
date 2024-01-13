from django.urls import path, include
from book import views

app_name = 'book'

urlpatterns = [
    # Function based index/newspaper view
    # ------------------------------------------------------------------------------------------------
    path('home/', views.index, name='index'),


    # Function based base_page view
    # ------------------------------------------------------------------------------------------------
    path('contact_form/',views.send_email,name='send_email'),


    # Function based magazine view
    # ------------------------------------------------------------------------------------------------
    path('magazine/', views.magazine, name='magazine'),


    # Function based comic view
    # ------------------------------------------------------------------------------------------------
    path('comic/',views.comic, name='comic'),


    # Function based detail_newspaper view
    # ------------------------------------------------------------------------------------------------
    path('detail/<int:item_id>/', views.detail, name='detail'),


    # Function based detail_m view
    # ------------------------------------------------------------------------------------------------
    path('detail_m/<int:magazine_id>/',views.detail_m, name='detail_m'),


    # Function based detail_c view
    # ------------------------------------------------------------------------------------------------
    path('detail_c/<int:comic_id>/',views.detail_c, name= 'detail_c'),


    # Function based Create_newspaper view
    # ------------------------------------------------------------------------------------------------
    path('add/',views.create_item, name='create_item'),


    # Function based Create_m view
    # ------------------------------------------------------------------------------------------------
    path('add_m/',views.create_magazine, name='create_magazine'),


    # Function based create_c view
    # ------------------------------------------------------------------------------------------------
    path('add_c/',views.create_comic, name="create_comic"),


    # Function based update_newspaper view
    # ------------------------------------------------------------------------------------------------
    path('update/<int:item_id>/',views.update_item, name="update_item"),


    # Function based update_m view
    # ------------------------------------------------------------------------------------------------
    path('update_magazine/<int:magazine_id>/',views.update_magazine, name="update_magazine"),


    # Function based update_c view
    # ------------------------------------------------------------------------------------------------
    path('update_comic/<int:comic_id>/',views.update_comic, name="update_comic"),


    # Function based delete_newspaper view
    # ------------------------------------------------------------------------------------------------
    path('delete/<int:item_id>/',views.delete_item, name='delete_item'),


    # Function based delete_m view
    # ------------------------------------------------------------------------------------------------
    path('delete_magazine/<int:magazine_id>/',views.delete_magazine,name='delete_magazine'),


    # Function based delete_c view
    # ------------------------------------------------------------------------------------------------
    path('delete_comic/<int:comic_id>/',views.delete_comic,name='delete_comic'),


    # Function based Contact view
    # ------------------------------------------------------------------------------------------------
    # path('contact/',views.contact_view, name='contact'),


    # Function based bookupload view
    # ------------------------------------------------------------------------------------------------
    path('upload/<int:detail_id>/', views.BookUploadView, name='bookupload'),


    path('newspaper/<int:item_id>/',views.news_views, name='news'),

    path('news_delete/<int:news_id>/<int:delete_id>/',views.delete_news, name='delete_news'),

    path('upload_comic/<int:detail_id>/',views.upload_comic, name='uploadcomic'),

    path('upload_magazine/<int:detail_id>/',views.upload_magazine, name='uploadmagazine'),

    path('about/',views.about, name='about'),

    path('contact/',views.contact, name='contact'),

    path('team/',views.team, name='team'),

]