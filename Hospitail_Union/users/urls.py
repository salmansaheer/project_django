from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='users_home'),
    path('info/', view_data, name='users_view'),
]
