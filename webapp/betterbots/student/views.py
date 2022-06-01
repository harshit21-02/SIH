from re import X
from django.http import HttpResponse
from django.shortcuts import redirect, render
from pytz import country_timezones
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

# Create your views here.


x=0

def studenthome(request):
    return render(request, "STUDENTS PAGE\home.html")

def application(request):
    if request.method=="POST":
        name:str =  request.POST['name'],
        dob      =  request.POST['dob'],
        mail :str    =  request.POST['mail'],
        contact  =  request.POST['contact'],
        password:str =  request.POST['password'],
        cnfpass  =  request.POST['cnfpass']



        global x
        x=x+1
        print(x)
        cno="052"
        appno="2022"+cno+str(x)
        
        
        msg=None
        password=str(password)

        myuser = User.objects.create_user(username=name, password = password)
        myuser.first_name = name
        myuser.mail=mail
        myuser.contact=contact
        myuser.is_student=True
        myuser.application_no=appno
        

        myuser.save()

        messages.success(request, "applied")

        return redirect('/student/iform')

    return render(request, "STUDENTS PAGE\pply.html")

def result(request):
    msg = None
    if request.method=="POST":
        username: str =  request.POST['username'],
        password =  request.POST['password'],
        password=str(password) 

        appn:str=username
        user =None
        user = authenticate(username=appn, password=password)
        if user is not None:
            login(request, user)
            msg='logged in'
            print(msg)
            return redirect('/student/iform')
        else:
            msg = 'invlaid credentials'
            print(msg)
            return redirect('/')  
    return render(request, "STUDENTS PAGE\index.html")

def iform(request):
    return render(request, "STUDENTS PAGE\iform.html")
