from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from taggit.managers import TaggableManager
# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    country = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name + ' ' + self.last_name 

class Category(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.category

class Post(models.Model):
    Title = models.CharField(max_length=255)
    Image = models.ImageField()
    Content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,null=True)
    tags = TaggableManager()
    author = models.ForeignKey(Member, on_delete=models.CASCADE ,null=True)
    date=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.Title

class ForbiddenWord(models.Model):
    forbidden_word = models.CharField(max_length=50)
    def __str__(self):
        return self.forbidden_word
