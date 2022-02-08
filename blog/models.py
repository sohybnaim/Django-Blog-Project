import email
from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone_number = models.IntegerField()
    country = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name + ' ' + self.last_name