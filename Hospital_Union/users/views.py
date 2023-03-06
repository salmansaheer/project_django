from django.shortcuts import render, redirect
from creator.models import GeneralDetails,Users

def my_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'userid' in request.session:
            id = request.session['userid']
            user = GeneralDetails.objects.get(pk=id)
            if user.role == 'admin':
                return redirect('creator_home')
            elif user.role == 'user':
                return view_func(request, *args, **kwargs)
            elif user.role == 'hospital':
                return redirect('hospitals_home')
            else:
                return redirect('guest_login')
        else:
            return redirect('guest_login')
    return wrapper

@my_login_required
def home(request):
    return render(request,'users/home.html')

def view_data(request):
    if request.method == 'GET':
        user_data=Users.objects.get(general_details_id=6)
        return render(request,'users/view.html',context={'user_data':user_data})

def view_medical_history(request):
    return render(request,'users/medical_history.html')