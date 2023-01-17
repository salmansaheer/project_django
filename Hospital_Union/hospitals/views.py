from django.shortcuts import render

def home(request):
    return render(request, 'hosptails/home.html')