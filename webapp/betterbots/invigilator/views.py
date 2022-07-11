from re import X
from django.http import HttpResponse
from django.shortcuts import redirect, render
from pytz import country_timezones
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
# Create your views here.

def inhome(request):
    msg = "fghj"
    if request.method=="POST":
        username: str =  request.POST['Center_ID']
        password =  request.POST['password']
        password=str(password) 
        print(username)
        print(password)
        
        user =None
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            data1=dict()
            data1['username']=user.get_username
            return redirect('/../invigilator/scan')
        else:
            msg = 'invlaid credentials'
            print(msg)
            return redirect('/')  
    return render(request, "INVIGILATOR\index.html")

def scan(request):
    # print(data['username'])
    return render(request, "INVIGILATOR\scan.html")