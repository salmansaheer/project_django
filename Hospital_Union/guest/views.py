from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from creator.models import GeneralDetails

def guest_home(request):
    return render(request, 'guest/home.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'guest/login_page.html')
    if request.method == 'POST':
        # user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        # if user is not None:
        #     login(request, user)
        #     if user.role == 'user':
        #         return redirect('users_home')
        #     elif user.role == 'hospital':
        #         return redirect('hospitals_home')
        # else:
        #     print('hi')
        # return render(request, 'guest/login_page.html', {'error': 'Invalid Username / Password'})

        user=GeneralDetails.objects.filter(username= request.POST['username'], password = request.POST['password'])
        if user:
            user = user[0]
            request.session['userid'] = user.general_details_id
            if user.role == 'user':
                return redirect('users_home')
            elif user.role == 'hospital':
                return redirect('hospitals_home')
        else:
            print("Not Exists")

        return render(request,'guest/login_page.html')
    

def logout(request):
    del request.session['userid']
    return redirect('guest_login')