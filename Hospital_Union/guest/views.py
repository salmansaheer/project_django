from django.shortcuts import render

def guest_home(request):
    return render(request, 'guest/home.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'guest/login_page.html')