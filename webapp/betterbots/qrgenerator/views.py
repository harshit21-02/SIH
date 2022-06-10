from django.shortcuts import render
import qrcode 

data=None
def qr(request):
    global data
    if request.method=="POST":
        data=request.POST['data']
        img=qrcode.make(data)
        img.save("static/qrcode/test.png")
    else:
        pass
    return render(request,"qr/index.html",{'data':data})

    # https://www.linkedin.com/in/harshit-chaurasia-165080214/