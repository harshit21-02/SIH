from email.mime import image
from re import X
from django.http import HttpResponse
from django.shortcuts import redirect, render
from pytz import country_timezones
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
import qrcode 
import PIL.Image
import cv2
from deepface import DeepFace
import os
from student.models import studata
 
from authenticate import models

from deepface import DeepFace
import cv2
import numpy as np
import os


def ahome(request):
    return render(request,"allocate/index.html")


def allocate(request):

    li = []
    c1 = os.getcwd() + str(r"\media\static\c1")
    c0 = os.getcwd() + str(r"\media\static\c0")
    cc1 = str(r"\static\c1")
    cc0 = str(r"\static\c0")

    for file in os.listdir(c1):
        for image in os.listdir(c1):
            recognition = DeepFace.verify(img1_path=os.path.join(c1, file), img2_path=os.path.join(c1, image))
            if recognition['verified'] == True:
                li.append((file, image))
    
    for file in os.listdir(c0):
        for image in os.listdir(c0):
            recognition = DeepFace.verify(img1_path=os.path.join(c0, file), img2_path=os.path.join(c0, image))
            if recognition['verified'] == True:
                li.append((file, image))
       

    li = [(i, j) for (i, j) in li if i != j]
    li = [(j, i) for (i, j) in li if j > i]
    li = [*set(li)]
             
    print('students at these image index should not be kept in same center', li)
    
    
    for (i, j) in li:
        if i and j in os.listdir(c1):
            img = cv2.imread(os.path.join(c1, i))
            os.chdir(c0)
            cv2.imwrite(i, img)
            os.remove(os.path.join(c1,i))
            i1=i
            i = i.replace('.jpg','')
            obj=studata.objects.get(username=i)
            obj.image=cc0+"\\"+i1
            obj.center=0
            obj.save()
            print('applicant', i, 'swaped')
        if i and j in os.listdir(c0):
            img = cv2.imread(os.path.join(c0, i))
            os.chdir(c1)
            cv2.imwrite(i, img)
            os.remove(os.path.join(c0, i))
            i1=i
            i = i.replace('.jpg', '')
            obj=studata.objects.get(username=i)
            obj.image=cc1+"\\"+i1
            obj.center=1
            obj.save()
            print('applicant', i, 'swaped')

    return HttpResponse(li)