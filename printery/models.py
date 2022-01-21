from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    phone_number = models.IntegerField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username}"

class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=64)

class Company(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=25)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=56)
    email = models.CharField(max_length=64)
    is_manufacturer = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class Order(models.Model):
    number = models.IntegerField()
    owner = models.ManyToManyField(User, blank=True, related_name="order_owners")
    BOOK = 'BK'
    CALENDR = 'CL'
    MAGAZINE = 'MZ'
    TYPE_CHOICES = [
        (BOOK, 'Book'),
        (CALENDAR, 'Calendar'),
        (MAGZAINE, 'Magazine'),
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        )
    title = models.CharField(max_length=16)
    amount = models.IntegerField()
    BINDING_STYLE_CHOICES = [
        ('GLU', 'Glue'),
        ('STA', 'Staple'),
        ('HAR', 'Hardcover'),
        ('FOL', 'Folding'),
    ]
    binding_style = models.CharField(
        max_length=3,
        choices=BINDING_STYLE_CHOICES,
        )
    final_width = models.IntegerField()
    final_height = models.IntegerField()
    num_pages_in_block = models.IntegerField()
    num_pages_in_cover = models.IntegerField()
    num_pages_in_insert = models.IntegerField()
    paper_block = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="block_paper")
    paper_cover = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="cover_paper")
    paper_insert = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="insert_paper")
    LAMINATE_CHOICES = [
        ('MAT', 'Matte'),
        ('GL', 'Glossy'),
    ]
    laminat = models.CharField(max_length=3,
        choiced=LAMINATE_CHOICES,
        )

class Paper(models.Model):
    name = models.CharField(max_length=64)
    TYPE_CHOICES = [
        ('GL', 'Glossy'),
        ('MAT', 'Matte'),
        ('OFF', 'Offset'),
    ]
    type = models.CharField(max_length=3,
        choiced=TYPE_CHOICES,
        )
    density = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    manufacturer = models.ManyToManyField(Company,blank=True, related_name="made_by")
