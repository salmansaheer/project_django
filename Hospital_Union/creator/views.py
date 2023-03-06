from django.shortcuts import render,redirect
from .forms import *
from django.views.generic import CreateView
from django.urls import reverse_lazy

def my_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'userid' in request.session:
            id = request.session['userid']
            user = GeneralDetails.objects.get(pk=id)
            if user.role == 'admin':
                return view_func(request, *args, **kwargs)
            elif user.role == 'user':
                return redirect('users_home')
            elif user.role == 'hospital':
                return redirect('hospitals_home')
            else:
                return redirect('guest_login')
        else:
            return redirect('guest_login')
    return wrapper


def creator_home(request):
    return render(request, 'creator/home.html')

def register_user(request):
    if request.method == 'GET':
        return render(request,'creator/user_registration.html',context={'users': USERS(),'generalinfo':GENERALDETAILS()})
    elif request.method == 'POST':
        users=USERS(data=request.POST,files=request.FILES)
        generalinfo=GENERALDETAILS(request.POST)
        if users.is_valid() and generalinfo.is_valid():
            obj1 = generalinfo.save(commit=False)
            obj1.role = 'user'
            obj2 = users.save(commit=False)
            obj2.general_details = obj1
            obj1.save()
            obj2.save()
            return render(request,'creator/home.html')
        else:
            return render(request,'creator/user_registration.html',context={'users':users,'generalinfo':generalinfo})
    return render(request,'creator/user_registration.html')

def register_hospital(request):
    if request.method == 'GET':
        return render(request,'creator/hospital_registration.html',context={'hospital': HOSPITAL(),'generalinfo':GENERALDETAILS()})
    elif request.method == 'POST':
        hospital=HOSPITAL(data=request.POST,files=request.FILES)
        generalinfo=GENERALDETAILS(request.POST)
        if hospital.is_valid() and generalinfo.is_valid():
            obj1 = generalinfo.save(commit=False)
            obj1.role = 'hospital'
            obj2 = hospital.save(commit=False)
            obj2.general_details = obj1
            obj1.save()
            obj2.save()
            return render(request,'creator/home.html')
        else:
            return render(request,'creator/hospital_registration.html',context={'hospital':hospital,'generalinfo':generalinfo})
    return render(request,'creator/hospital_registration.html')
