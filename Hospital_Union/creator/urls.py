from django.urls import path
from .views import *

urlpatterns = [
    path('', creator_home, name='creator_home'),
    path('register/',register_user,name='creator_register_user'),
    # path('register/',ProductCreateView.as_view(),name='creator_register_user'),
]