from operator import truediv
from django.conf import settings
from django.core.mail import send_mail

def send_email_token(email, token):
    try:  
        subject = 'Login Attempt using your center credentials'
        print('mailed')
        message = f'Click on the link to verify http://127.0.0.1:8000/evaluator/verify'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        print(recipient_list)
        send_mail( subject, message, email_from, recipient_list )
    except Exception as e:
        return False
    
    return True
