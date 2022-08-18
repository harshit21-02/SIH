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

# Create your views here.

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
<<<<<<< HEAD
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
=======
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

>>>>>>> aaa1d3a3a0d2d6d823ed281054efcb750381ae75
    while True:
        _, img = cam.read()
        cv2.imshow("img", img)
        if cv2.waitKey(1) == ord("s"):
<<<<<<< HEAD
            cv2.imwrite('image.jpg' ,img)
            # df = DeepFace.verify(img_path = "E:\SIH\SIH\SIH\webapp\image.jpg", db_path = "E:/SIH/SIH/SIH/webapp/betterbots/static/STUDENTS PAGE/images")
            # print(df)
            # obj = DeepFace.analyze(img_path = "image.jpg", actions = ['age', 'gender', 'race', 'emotion'])
            result = DeepFace.verify(img2_path=r'E:\SIH\SIH\SIH\webapp\image.jpg',img1_path=r'E:\SIH\SIH\SIH\webapp\betterbots\static\STUDENTS PAGE\images\WhatsApp_Image_2022-07-12_at_4.02.35_PM.jpeg')
            # print(obj)
            if result['verified']==True:
                print('matched')
                break
            else:
                print('NOT VERIFIED')
                break

        if cv2.waitKey(1) == ord("q"):
            break
    cam.release()
    cv2.destroyAllWindows()
=======
            cv2.imwrite('image.jpg', img)
            break
    cam.release()
    cv2.destroyAllWindows()
    s = 0
    path = r"C:\Users\Prateek Pal\SIH\webapp\betterbots\media\pictures\\"
    for file in os.listdir(path):
        recognition = DeepFace.verify(img1_path="image.jpg", img2_path=path + str(file))
        if recognition['verified'] == True:
            print('Verified!!! for the image', file)
            s = 1
            break
    if s == 0:
        print("No Data found -_-")
>>>>>>> aaa1d3a3a0d2d6d823ed281054efcb750381ae75
    if data!="":
        return HttpResponse(data)

    return redirect('/../invigilator/scan')
    
def details(data):
    print(data)
    return HttpResponse(data)    
