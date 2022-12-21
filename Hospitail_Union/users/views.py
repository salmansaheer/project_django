from django.shortcuts import render

def home(request):
    return render(request, 'users/home.html')
# Create your views here.

def view_data(request):
    context={}
    return render(request,'users/view.html',context)