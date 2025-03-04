from django.db import models
from django.contrib.auth.models import AbstractUser, User
import random
import string
from django.contrib.auth import get_user_model
from django.utils.timezone import now, timedelta


class CUSTOMUSER(AbstractUser):
    phone_no = models.CharField(max_length =13,blank=True,null =True)
    

    def __str__(self):
        return self.username

class PROFILE(models.Model):
    GENDER =[
            ("Male","male"),
            ("Female","female"),
            ("Other","other"),
            ]
    image = models.ImageField(upload_to= "profile_pic/")
    name = models.CharField(max_length =230, null =True, blank =True)
    age = models.CharField(max_length = 3)
    gender = models.CharField(max_length =10, choices =GENDER)
    user = models.ForeignKey(CUSTOMUSER,on_delete=models.CASCADE,related_name="profile",db_index=True)
    
# Changes from here, Direct Chatgpt

class QuizResponse(models.Model):
    user = models.ForeignKey(CUSTOMUSER, on_delete=models.CASCADE, related_name="quiz_responses")
    
    primary_skin_concern = models.CharField(max_length=100)
    skin_type = models.CharField(max_length=50)
    breakout_frequency = models.CharField(max_length=50)
    reaction_to_skincare = models.CharField(max_length=100)
    redness_inflammation = models.CharField(max_length=100)
    sunscreen_usage = models.CharField(max_length=100)
    skin_conditions = models.CharField(max_length=100)
    after_washing_skin_feel = models.CharField(max_length=100)
    water_intake = models.CharField(max_length=50)
    dark_spots_pigmentation = models.CharField(max_length=100)
    visible_pores = models.CharField(max_length=100)
    exfoliation_frequency = models.CharField(max_length=50)
    fine_lines_wrinkles = models.CharField(max_length=100)
    dairy_processed_food_intake = models.CharField(max_length=100)
    skincare_routine = models.CharField(max_length=100)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Quiz Response {self.id}"

# Upto here
User = get_user_model()

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return now() < self.created_at + timedelta(minutes=5)  # OTP expires in 5 minutes

    def __str__(self):
        return f"OTP for {self.user.username}: {self.code}"
