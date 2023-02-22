from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='hospitals_home'),
    path('login/',hospital_login,name='guest_login'),
    # path('admin/', home, name='hospitals_home'),
    path('admin/view_staff/', view_staff, name='hospitals_view_staff'),
    path('admin/add_staff/', add_staff, name='hospitals_add_staff'),
    path('admin/remove_staff/', remove_staff, name='hospitals_remove_staff'),
    path('admin/view_doctors/', view_doctors, name='hospitals_view_doctors'),
    path('admin/add_doctors/', add_doctors, name='hospitals_add_doctors'),
    path('admin/remove_doctors/', remove_doctors, name='hospitals_remove_doctors'),
    path('staff/add_doc/', add_doc, name='hospitals_add_doc')
]
