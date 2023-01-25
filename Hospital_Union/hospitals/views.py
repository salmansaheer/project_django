from django.shortcuts import render

def home(request):
    return render(request, 'hospitals/home.html')