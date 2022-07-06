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
    lastname=models.TextField('last_name',max_length=30,default='')
    dob=models.DateField('dob',default='2001-1-1')
    email=models.EmailField('email',max_length=30,default='')
    contact=models.TextField('contact',default='')
    center=models.TextField('center',max_length=30,default='')
    image=models.ImageField(upload_to="static/STUDENTS PAGE/images/",null=True,blank=True)
    
    def __str__(self):
        return self.appno
    
