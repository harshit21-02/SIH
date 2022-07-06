from dataclasses import dataclass
from re import X
from django.http import HttpResponse
from django.shortcuts import redirect, render
from pytz import country_timezones
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from student.models import studata

User = get_user_model()

# Create your views here.


x=0

def studenthome(request):
    return render(request, "STUDENTS PAGE\home.html")

def application(request):
    if request.method=="POST":
        username:str =  request.POST['username']
        fname:str = request.POST['fname']
        lname:str = request.POST['lname']
        dob: str =  request.POST['dob']
        mail :str = request.POST['mail']
        contact  =  request.POST['contact']
        password:str =  str(request.POST['password'])
        cnfpass: str = str(request.POST['cnfpass'])
        

        
        print(cnfpass)
        print(password)
        global x
        x=x+1
        print(x)
        cno="052"
        appno="2022"+cno+str(x)
        
        msg=None
        password=str(password)

        if password !=cnfpass:
            return redirect('/../student/application/')

        myuser = User.objects.create_user(username=username, password = password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.email=mail
        myuser.dob=dob
        myuser.contact=contact
        myuser.is_student=True
        myuser.application_no=appno
        
        myuser.save()

        center:str=(str)('to be assigned')
        
        sdata=studata()
        sdata.appno=appno
        sdata.firstname=fname
        sdata.lastname=lname
        sdata.dob=dob
        sdata.email=mail
        sdata.contact=contact
        sdata.center=center
        if len(request.FILES)!=0:
            sdata.image=request.FILES['image']
        sdata.save()

        messages.success(request, "applied")

        return redirect('/../student/iform/')

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
            data1=dict()
            data1['username']=user.get_username
            return redirect('/../student/iform/')
        else:
            msg = 'invlaid credentials'
            print(msg)
            return redirect('/')  
    return render(request, "STUDENTS PAGE\index.html")

def iform(request):
    # print(data['username'])
    return render(request, "STUDENTS PAGE\iform.html")
