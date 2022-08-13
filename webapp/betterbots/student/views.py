from dataclasses import dataclass
from re import X
import re
from xml.dom import ValidationErr
from django.http import HttpResponse
from django.shortcuts import redirect, render
from pytz import country_timezones
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from student.models import studata
from django import forms
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.


x=0

def studenthome(request):
    return render(request, "STUDENTS PAGE\home.html")

def application(request):
    
    if request.method=="POST":
        username =  request.POST['username']
        fname:str = request.POST['fname']
        # lname:str = request.POST['lname']
        dob: str =  request.POST['dob']
        mail :str = request.POST['mail']
        contact  =  request.POST['contact']
        password:str =  str(request.POST['fpassword'])
        cnfpass: str = str(request.POST['spassword'])
        gender:str = request.POST['gender']
        state:str = request.POST['state']
        # pincode:str = request.POST['pin']
        city:str = request.POST['city']
        ntly:str = request.POST['ntly']


        if User.objects.filter(username=username).exists():
            messages.error(request, ' Sorry! Username is already taken')
            return redirect('/student/application')
        elif User.objects.filter(email=mail).exists():
            messages.error(request, ' Sorry! Email is already registered')
            return redirect('/student/application')

        global x
        x=x+1
        cno="052"
        appno="2022"+cno+str(x)
        
        msg=None
        password=str(password)


        # if password !=cnfpass:
        #     try:
        #     except ValidationError:


            # return redirect('/../student/application/')

        myuser = User.objects.create_user(username = username, password = password)
        myuser.fullname=fname
        # myuser.last_name=lname
        myuser.email=mail
        myuser.dob=dob
        myuser.contact=contact
        myuser.password = password
        myuser.gender = gender
        # myuser.pincode = pincode
        # myuser.landmark = landmark
        myuser.state = state
        # myuser.adress1 = adress1
        # myuser.adress2 = adress2
        myuser.is_student=True
      
        
        myuser.application_no=appno
        if len(request.FILES)!=0:
            myuser.image=request.FILES['image']
        
        myuser.save()

        center:str=(str)('to be assigned')
        
        sdata=studata()
        sdata.appno=appno
        sdata.fullname=fname
        sdata.email=mail
        sdata.dob=dob
        sdata.contact=contact
        sdata.password = password
        sdata.gender = gender
        # sdatax.pincode = pincode
        # sdata.landmark = landmark
        sdata.state = state
        # sdata.adress1 = adress1
        # sdata.adress2 = adress2
        sdata.center=center
        if len(request.FILES)!=0:
            sdata.image=request.FILES['image']
        sdata.save()
        return redirect('/../student/result')
    return render(request, "STUDENTS PAGE\pply.html")

def result(request):
    msg = None
    
    if request.method=="POST":
        username =  request.POST['username']
        password =  request.POST['password']
        # password=str(password) 
        # username=str(username)
        user = authenticate(request,username=username, password=password)
        if user is not None:
            if user.is_student==False:
                msg = 'Unauthorized'
                print(msg)
                messages.info(request,'User is UNAUTHORIZED!')
                return redirect('/../student/result')
            login(request, user)
            data1=dict()
            print('LOGGED IN')

            return redirect('/../student/profile')
        else:
            messages.info(request,'User is not registered!')
            return redirect('/../student/result')
            
    return render(request, "STUDENTS PAGE\index.html")

def logout1(request):
    logout(request)
    messages.info(request,'Successfully logged out!')
    return redirect('/../student/result')

def profile(request):
    if request.user.is_authenticated:
        return render(request, "STUDENTS PAGE\iform.html")
    else:
        msg = 'Unauthorized'
        print(msg)
        messages.info(request,'UNAUTHORIZED!')
        return redirect('/../student/result')


# dict = {'Name':[],'Contact':[]}
# dict['name'].append()

# def create_df(request):
    

