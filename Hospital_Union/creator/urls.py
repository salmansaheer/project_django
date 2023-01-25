from django.urls import path
from .views import *

urlpatterns = [
    path('', creator_home, name='creator_home'),
    path('register/',register,name='creator_register'),
]