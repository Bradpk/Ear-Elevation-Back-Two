from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
#------------------------------------------------------------------------------------------------------------------------------
class CustomUser(AbstractUser):
    def __str__(self):
        return self.email
#------------------------------------------------------------------------------------------------------------------------------
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_registered = models.DateTimeField()
#------------------------------------------------------------------------------------------------------------------------------
class UserLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    exercise_id = models.CharField(max_length=100)
    date_completed = models.CharField(max_length=100)
    total_questions = models.CharField(max_length=100)
    correct_answers = models.CharField(max_length=100)
    percentage_correct = models.CharField(max_length=200)


