from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    phone_number = models.IntegerField()

    def __str__(self):
        return f"{self.username}"

class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=64)

class Customer(models.Model):
    customer_name = models.CharField(max_length=64)
    contact_name = models.CharField(max_length=16)
    email = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=25)
    postal_code = models.IntegerField(max_length=6)
    country = models.CharField(max_length=56)

class Order(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=16)
    title = models.CharField(max_length=16)
    amount = models.IntegerField()
