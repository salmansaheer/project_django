from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='hospitals_home'),
]
