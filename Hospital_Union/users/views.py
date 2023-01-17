from django.shortcuts import render


def home(request):
    return render(request, 'users/home.html')

def view_data(request):
    context={}
    return render(request,'users/view.html',context)