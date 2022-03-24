from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    password= models.CharField(max_length=32)
    email= models.CharField(max_length=50)


class Home(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    
