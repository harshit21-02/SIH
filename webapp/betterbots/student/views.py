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
        dob: str =  request.POST['dob']
        mail :str = request.POST['mail']
        contact  =  request.POST['contact']
        gender:str = request.POST['gender']
        password:str =  str(request.POST['fpass'])
        cnfpass: str = str(request.POST['spass'])
        city:str = request.POST['city']
        state:str = request.POST['state']
<<<<<<< HEAD

=======
>>>>>>> ab9877c7146b6d936710ce3f08171cc3af07428f
        ntly:str = request.POST['ntly']

        if(password != cnfpass):
            messages.error(request, 'Password and Confirm password are not same!')
            return redirect('/student/application')
        
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
        myuser.dob=dob
        myuser.email=mail
        myuser.contact=contact
<<<<<<< HEAD

=======
>>>>>>> ab9877c7146b6d936710ce3f08171cc3af07428f
        myuser.gender=gender
        myuser.city = city
        myuser.state = state
        myuser.nationality = ntly
        myuser.password = password
<<<<<<< HEAD
=======

>>>>>>> ab9877c7146b6d936710ce3f08171cc3af07428f
        myuser.is_student=True
      

        myuser.application_no=appno
        if len(request.FILES)!=0:
            myuser.image=request.FILES['image']
        
        myuser.save()

        center:str=(str)('to be assigned')
        # sdata = studata.objects.create_user(username = username, password = password)
        sdata=studata()
        sdata.appno=appno
        sdata.username = username
        sdata.fullname=fname
        sdata.dob=dob
        sdata.email=mail
        sdata.contact=contact
        sdata.gender = gender
        sdata.city = city
        sdata.state = state
<<<<<<< HEAD
        sdata.password = password
=======
        sdata.nationality = ntly
        # sdata.password = password
>>>>>>> ab9877c7146b6d936710ce3f08171cc3af07428f

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
            posts=studata.objects.filter(username=username,password=password)
            print('LOGGED IN')

            return redirect('/../student/profile',posts)
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
    

