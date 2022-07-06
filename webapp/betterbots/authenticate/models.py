from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    application_no=models.TextField('application_no',default='')
    dob=models.DateField('dob',default='2001-1-1')
    contact=models.TextField('contact',default='')
    centre=models.TextField('centre',default='')
    is_student=models.BooleanField('is_student',default=False)
    is_invigilator=models.BooleanField('is_invigilator',default=False)
    is_evaluator=models.BooleanField('is_evaluator',default=False)

    
    
    
