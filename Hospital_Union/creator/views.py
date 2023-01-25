from django.shortcuts import render

def creator_home(request):
    return render(request, 'creator/home.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'creator/login_page.html')
    