from asyncio.windows_events import NULL
from curses.ascii import NUL
from distutils.command.upload import upload
import email
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import ImageField

# Create your models here.

class studata(models.Model):
    appno=models.TextField('appno',max_length=30,default='')
    firstname=models.TextField('first_name',max_length=30,default='')
    # lastname=models.TextField('last_name',max_length=30,default='')
    dob=models.DateField('dob',default='2001-1-1')
    email=models.EmailField('email',max_length=30,default='')
    contact=models.TextField('contact',default='')
    city=models.TextField('city', default = '')
    state=models.TextField('state', default='')
    country=models.TextField('country', default='')
    pincode=models.TextField('pin',max_length = 6, default='')
    password=models.TextField('pass', default='')
    landmark=models.TextField('ld_mark', default='')
    adress1=models.TextField('ad1', default='')
    adress2=models.TextField('ad2', default='')
    center=models.TextField('center',max_length=30,default='')
    gender=models.TextField('gender',max_length=10,default='')
    image=models.ImageField(upload_to="static/STUDENTS PAGE/images/",null=True,blank=True)

    
    def __str__(self):
        return self.appno
    
    