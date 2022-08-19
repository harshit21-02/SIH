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

from django.conf import settings
value = settings.BASE_DIR
# Create your views here.

posts={}

def inhome(request):
    msg = "fghj"
    if request.method=="POST":
        username: str =  request.POST['Center_ID']
        password =  request.POST['password']
        password=str(password) 
        # print(username)
        # print(password)
        
        user =None
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_invigilator==False:
                msg = 'Unauthorized'
                print(msg)
                messages.info(request,'User is UNAUTHORIZED!')
                print("UNAUTHORIZED")
                return redirect('/../invigilator/') 
            login(request, user)
            return redirect('/../invigilator/scan')
        else:
            msg = 'invlaid credentials'
            print(msg)
            messages.info(request,'User is not registered!')
            return redirect('/../invigilator/')  
    return render(request, "INVIGILATOR\index.html")

def scan(request):
    if request.user.is_authenticated:
        return render(request, "INVIGILATOR\scan.html")
    else:
        msg = 'Unauthorized'
        print(msg)
        messages.info(request,'UNAUTHORIZED!')
        return redirect('/../invigilator/') 
    

def logo(request):
    logout(request)
    messages.info(request,'Successfully logged out!')
    return redirect('/../invigilator/')



def video_reader(request):
    print("HELLO WORLD")
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    detector = cv2.QRCodeDetector()
    data=""
    while True:
        _, img = cam.read()
        cv2.imshow("img", img)
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            print("QR Code detected-->", data)
            break
        if cv2.waitKey(1) == ord("q"):
            break
    cam.release()
    cv2.destroyAllWindows()

    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    while True:
        _, img = cam.read()
        cv2.imshow("img", img)
        if cv2.waitKey(1) == ord("s"):
            cv2.imwrite('image.jpg', img)
            break
    cam.release()
    cv2.destroyAllWindows()
    s = 0
    path = os.path.join(os.path.dirname(value), 'betterbots','media', 'static', 'STUDENTS PAGE', 'images/')
    for file in os.listdir(path):
        path1 = os.path.join(os.path.dirname(value), 'betterbots','media', 'static', 'STUDENTS PAGE', 'images', file)
        # print(path1)
        recognition = DeepFace.verify(img1_path="image.jpg", img2_path=path1, enforce_detection=False)
        if recognition['verified'] == True:
            posts['impath']=path1
            print('Verified!!! for the image', file)
            s = 1
            return redirect('/../invigilator/details')
    if s == 0:
        print("No Data found -_-")
        
    if data!="":
        return HttpResponse(data)

    return redirect('/../invigilator/scan')
    
def details(request):
    post=studata.objects.get(image=posts['impath'])
    print(post)
    return render(request, "INVIGILATOR/finald.html",post)  
