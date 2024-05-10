from django.db import models

# Create your models here.
# aptitude_test/models.py

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=200, default='')

class College(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    required_score = models.IntegerField()
