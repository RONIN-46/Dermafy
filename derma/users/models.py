from django.db import models
from django.contrib.auth.models import AbstractUser



class CUSTOMUSER(AbstractUser):
    phone_no = models.CharField(max_length =13,blank=True,null =True)

    def __str__(self):
        return self.username


