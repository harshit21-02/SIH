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

def logo(request):
    logout(request)
    return redirect('/../invigilator/')



def video_reader(request):
    # print("HELLO WORLD")
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    detector = cv2.QRCodeDetector()
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
    if data:
        return redirect('/../invigilator/details',data=data)

    return redirect('/../invigilator/scan')
    

def details(data):
    print(data)
    return HttpResponse(data)    

    