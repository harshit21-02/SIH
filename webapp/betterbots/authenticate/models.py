from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    application_no=models.TextField('application_no',default='')
    fullname=models.TextField('full_name',max_length=30,default='')
    # lastname=models.TextField('last_name',max_length=30,default='')
    dob=models.DateField('dob',default='2001-1-1')
    contact=models.TextField('contact',default='')
    centre=models.TextField('centre',default='')
    email=models.EmailField('email',max_length=30,default='')
    country=models.TextField('country', default='')
    pincode=models.TextField('pincode',max_length = 6, default='')
    city=models.TextField('city', default = '')
    state=models.TextField('state', default='')
    is_student=models.BooleanField('is_student',default=False)
    is_invigilator=models.BooleanField('is_invigilator',default=False)
    is_evaluator=models.BooleanField('is_evaluator',default=False)
    image=models.ImageField(upload_to="static/STUDENTS PAGE/images/",null=True,blank=True)
    
    
    
