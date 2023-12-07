from django.db import models

# Create your models here.

class reg(models.Model):
    fullname = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
