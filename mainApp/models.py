from django.db import models

# Create your models here.
class Player(models.Model): #model also means table
    username = models.CharField(max_length= 20) #char is short for character/letter
    password = models.CharField(max_length= 50)
    profile_pic =models.ImageField()

class Resource(models.Model):
    name = models.CharField(max_length = 6)
    points = models.IntegerField() #integer/number

class Movie(models.Model):
    name = models.CharField(max_length = 6)
    description = models.TextField()

