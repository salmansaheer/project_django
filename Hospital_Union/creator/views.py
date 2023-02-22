from django.shortcuts import render
from .forms import *
from django.views.generic import CreateView
from django.urls import reverse_lazy

def creator_home(request):
    return render(request, 'creator/home.html')

def register_user(request):
    if request.method == 'GET':
        return render(request,'creator/user_registration.html',context={'users': USERS(),'generalinfo':GENERALDETAILS()})
    elif request.method == 'POST':
        users=USERS(data=request.POST,files=request.FILES)
        generalinfo=GENERALDETAILS(request.POST)
        if users.is_valid() and generalinfo.is_valid():
            obj1 = generalinfo
            print(obj1)
            obj1.role = 'user'
            obj1.save()
            obj2 = users
            obj2.general_details = obj1.general_details_id
            obj2.save()
            
            return render(request,'creator/home.html')
        else:
            return render(request,'creator/user_registration.html',context={'users':users,'generalinfo':generalinfo})
    return render(request,'creator/user_registration.html')
