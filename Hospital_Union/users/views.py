from django.shortcuts import render
from creator.models import GeneralDetails,Users

def home(request):
    return render(request,'users/home.html')

def view_data(request):
    if request.method == 'GET':
        user_data=Users.objects.get(general_details_id=1)
        return render(request,'users/view.html',context={'user_data':user_data})

def view_medical_history(request):
    return render(request,'users/medical_history.html')