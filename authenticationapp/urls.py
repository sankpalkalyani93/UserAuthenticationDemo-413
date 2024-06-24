from django.urls import path
from .views import login_view, home_view, register_view, logout_view, password_change_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name="logout"),
    path('', home_view, name='home'),
    path('password_change/', password_change_view, name='password_change'),
]
