from django.db import models
from django.contrib.auth.models import AbstractUser



class CUSTOMUSER(AbstractUser):
    phone_no = models.CharField(max_length =13,blank=True,null =True)

    def __str__(self):
        return self.username

class PROFILE(models.MODEL):
    GENDER =[
            ("Male","male"),
            ("Female","female"),
            ("Other","other"),
            ]
    image = models.ImageField(upload_to= "/profile_pic",default = )
    name = models.CharField(max_length =230, null =True, Blank =True)
    age = models.CharField(max_length = 3)
    gender = models.CharField(max_length =10, choices =GENDER)
    user = models.ForeignKey(CUSTOMUSER,on_delete=models.CASCADE,related_name="profile",db_index=True)
    
