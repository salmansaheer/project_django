from django.urls import path
from .views import *

urlpatterns = [
    path('', guest_home, name='guest_home'),
    path('login/',login,name='guest_login'),
]
