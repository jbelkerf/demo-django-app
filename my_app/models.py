from django.db import models
from unicodedata import name


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length = 100)
    cuisine = models.CharField(max_length = 100)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name + ":" + self.cuisine
    
class Person(models.Model):
    user_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 12)
    age = models.IntegerField(default = 20)

    def __str__(self) -> str:
        return self.user_name + "-->" + self.email