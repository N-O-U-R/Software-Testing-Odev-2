from django.urls import path
from accounts.views import user_login, register,logout_view

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
]
