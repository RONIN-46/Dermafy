from django.db import models
from django.contrib.auth.models import AbstractUser, User



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
    
# Changes from here, Direct Chatgpt
class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quizzes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)  # Mark correct answers

    def __str__(self):
        return self.text

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - {self.question.text}"

# Upto here
