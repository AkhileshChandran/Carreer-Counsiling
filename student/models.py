from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=25)
    age = models.PositiveIntegerField()
    options = (
        ("male","male"),("female","female"),("others","others")
    )
    gender = models.CharField(max_length=20,choices=options,default="male")
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    qualification = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    resume = models.FileField(upload_to="files",null=True)
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING,null=True,related_name="profile")

# 9097sree