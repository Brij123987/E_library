from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns = [
    path('register/',views.register, name="register"),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('profile/',views.profilepage, name='profile'),
    path('<int:pk>/',views.ProfileUpdateView.as_view(), name='update'),
]