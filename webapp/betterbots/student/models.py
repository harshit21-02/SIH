from asyncio.windows_events import NULL
from curses.ascii import NUL
import email
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class studata(models.Model):
    appno=models.TextField(max_length=30,default='')
    firstname=models.TextField(max_length=30,default='')
    lastname=models.TextField(max_length=30,default='')
    dob=models.DateField(default='2001-1-1')
    email=models.EmailField(max_length=30,default='')
    contact=models.TextField(default='')
    center=models.TextField(max_length=30,default='')
    
    
