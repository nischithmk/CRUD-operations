from django.db import models
from django.contrib.auth.models import AbstractUser

#user model
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

#adding book
class Book(models.Model):
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 30)
    email = models.EmailField(blank = True)
    describe = models.TextField()
    picture = models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return self.name