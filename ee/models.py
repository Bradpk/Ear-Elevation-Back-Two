from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    def __str__(self):
        return self.email
#---------------------------------------
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    # username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    date_registered = models.DateTimeField()

class Excercise(models.Model):
    excercise_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    description = models.TextField()

class UserLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    excercise_id = models.ForeignKey(Excercise, on_delete=models.CASCADE)
    date_completed = models.DateTimeField()
    total_questions = models.IntegerField()
    correct_answers = models.IntegerField()

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    excercise_id = models.ForeignKey(Excercise, on_delete=models.CASCADE)
    audio_text = models.CharField(max_length=255)

class Option(models.Model):
    option_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_option = models.CharField(max_length=255)
    is_correct = models.BooleanField()


#----------------

class Test(models.Model):
    test_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)

