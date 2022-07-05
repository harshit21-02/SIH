from email.mime import image
from tkinter import Image
from tkinter.tix import IMAGE
from django.shortcuts import render
import qrcode 
import PIL.Image
from qrgenerator.models import qrc


no=6
data=None
def qr(request):
    global data
    global no
    if request.method=="POST":
        no=no+1
        data=request.POST['data']
        img=qrcode.make(data)
        name: str = "test"+ str(no) +".png"
        img.save("static/qrcode/test.png")
        image_data: IMAGE = open("static/qrcode/test.png", "rb").read()
        # print(image_data)
        # qrc(serialn=name, qr_code = image_data).save()
    else:
        pass
    return render(request,"qr/index.html",{'data':data})

    # https://www.linkedin.com/in/harshit-chaurasia-165080214/