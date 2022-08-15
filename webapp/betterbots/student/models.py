from asyncio.windows_events import NULL
from curses.ascii import NUL
from distutils.command.upload import upload
import email
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import ImageField
from django.contrib.auth.models import User 

# Create your models here.

class studata(models.Model):
    # user=models.OneToOneField(User, on_delete=models.CASCADE)
    appno=models.TextField('appno',max_length=30,default='')
    username = models.TextField('username',max_length=10, default = '')
    fullname=models.TextField('full_name',max_length=30,default='')
    dob=models.DateField('dob',default='2001-1-1')
    email=models.EmailField('email',max_length=30,default='')
    contact=models.TextField('contact',default='')
    gender=models.TextField('gender', default = '')
    city=models.TextField('city', default = '')
    state=models.TextField('state', default='')
    nationality = models.TextField('ntly', default = '')
    image=models.ImageField(upload_to="static/STUDENTS PAGE/images/",null=True,blank=True)
    aid = models.TextField('aid', default = '')

    
    def __str__(self):
        return self.appno
    
    