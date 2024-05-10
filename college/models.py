from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CollegeModel(models.Model):
    name = models.CharField(max_length=25)
    location = models.CharField(max_length=200)
    contact = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
# Mes_Ponnani_college
# Mes2023