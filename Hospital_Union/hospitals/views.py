from django.shortcuts import render,redirect
from .models import StaffsAndDoctors

def home(request):
    return render(request, 'hospitals/home.html')

def hospital_login(request):
    if request.method == 'GET':
        return render(request, 'hospitals/hospital_login.html')
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        data=StaffsAndDoctors.objects.get(uname= username)
        if data.uname == username and data.password == password:
            if data.role == 'user':
                return redirect('users_home')
            if data.role == 'hospital':
                return redirect('hospitals_home')
        else:
            return render(request, 'hospitals/hospital_login.html', {'error': 'Invalid Username / Password'})

def about(request):
    return render(request, 'hospitals/about.html')

def view_staff(request):
    return render(request,'hospitals/view_staff.html' )

def add_staff(request):
    return render(request,'hospitals/add_staff.html' )
    
def remove_staff(request):
    return render(request,'hospitals/remove_staff.html' )
    
def view_doctors(request):
    return render(request,'hospitals/view_doctors.html' )

def add_doctors(request):
    return render(request,'hospitals/add_doctors.html' )
    
def remove_doctors(request):
    return render(request,'hospitals/remove_doctors.html' )

def add_doc(request):
    return render(request,'hospitals/remove_doctors.html' )
    