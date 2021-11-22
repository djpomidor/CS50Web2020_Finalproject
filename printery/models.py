from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    phone_number = models.IntegerField()
    


    def __str__(self):
        return f"{self.username}"
