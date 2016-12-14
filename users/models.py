from django.db import models


# Create your models here.

class users(models.Model):
    id = models.CharField(max_length=64,primary_key=True)
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
