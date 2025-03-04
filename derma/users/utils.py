import random
import string
from django.core.mail import send_mail
from .models import OTP

def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

def send_otp_email(user):
    otp_code = generate_otp()


    OTP.objects.create(user=user, code=otp_code)

    subject = "Your One-Time Password (OTP)"
    message = f"Your OTP code is: {otp_code}. It will expire in 5 minutes."
    from_email = "your-email@gmail.com"
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)
