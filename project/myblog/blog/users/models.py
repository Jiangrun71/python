from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=16)
    nickname = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11, null=True)
    email = models.EmailField()
    age = models.IntegerField()
    sex = models.BooleanField()
    character = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)

